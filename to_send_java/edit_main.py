# <main.py>
# uvicorn main:app --reload

# link fastapi + spring boot server
# > 1. chatbot.html, chatbot.css, chatbot.js 다 다운로드-> 폴더 안 맞추면 chatbot.html, js 교체해야, 열어놓기
# > 2. Live Server 확장 설치
# > 3. uvicorn edit_main.py --reload
# > 4. 창 자동으로 열림

import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import ChatCompletion, OpenAI
# from dotenv import load_dotenv
import logging
import os
from dotenv import load_dotenv

# Simple in-memory cache
cache = {}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# OpenAI API key setup
# Load API key from JSON file
# with open('openai_key.json', 'r') as file:
#     keys = json.load(file)

# API_KEY = keys['OPENAI_API_KEY']
# OpenAI API key setup
# # Initialize OpenAI client
# client = OpenAI(api_key=API_KEY)
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=API_KEY)


# FastAPI app setup
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FastAPI models
class UserRequest(BaseModel):
    utterance: str
    gu: str

class BotResponse(BaseModel):
    bot_message: str

class MedicalDepartment(BaseModel):
    name: str
    link: str

# Define medical departments and their links
# medical_departments = [
#     MedicalDepartment(name="이비인후과", link="file:///C:/Users/user/Desktop/Soobp9-saltlux_sessac_1-front/html/map.html"),
#     # Add other departments similarly
#     MedicalDepartment(name="내과", link="https://map.naver.com/p/search/%EA%B8%88%EC%B2%9C%EA%B5%AC%20%EB%82%B4%EA%B3%BC?searchType=place&c=13.00,0,0,0,dh"),
#     # Add other departments similarly
#     MedicalDepartment(name="치과", link="file:///C:/Users/user/Desktop/Soobp9-saltlux_sessac_1-front/html/hospital.html"),
#     # Add other departments similarly
# ]

# Queue object creation
response_queue = []

# Template directory setup
templates = Jinja2Templates(directory="templates")

# Maximum number of previous exchanges to keep
MAX_HISTORY_LENGTH = 7

# Function to trim the conversation history
def trim_conversation_history():
    global response_queue
    if len(response_queue) > MAX_HISTORY_LENGTH:
        # Keep only the last MAX_HISTORY_LENGTH exchanges
        response_queue = response_queue[-MAX_HISTORY_LENGTH:]

# Root endpoint for rendering HTML
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Chatbot endpoint
@app.post('/chatbot/', response_model=BotResponse)
async def chat(user_request: UserRequest):
    user_question = user_request.utterance.strip()
    gu = user_request.gu.strip()

    logger.debug(f'Received POST request: {user_question}')

    if user_question:
        # Call trim function before appending new response to ensure the queue length is maintained
        trim_conversation_history()

        gpt_answer, department = get_qa_by_gpt(user_question, gu)
        response_queue.append(gpt_answer)  # Now the queue will never exceed MAX_HISTORY_LENGTH
        logger.debug(f'Response queue: {response_queue}')
        return JSONResponse(content={'bot_message': gpt_answer, 'department':department, 'gu': gu})
    else:
        return JSONResponse(content={'bot_message': 'No input received', 'department': '', 'gu': ''})

# Additional endpoint to get the response
@app.get('/response/', response_class=JSONResponse)
async def get_response():
    if response_queue:
        return JSONResponse(content={'bot_message': response_queue.pop(0)})
    else:
        return JSONResponse(content={'bot_message': 'No response'})

# Function to get Q&A from GPT
def get_qa_by_gpt(prompt, gu, temperature=0.3, top_p=0.5, max_tokens=200, frequency_penalty=0.6, presence_penalty=0.1, stop=None, n=1):
    # Include the conversation history in the prompt
    conversation_history = "".join(response_queue)
    full_prompt = conversation_history + "\nUser: " + prompt + "\nAssistant: "

    cache_key = (prompt, temperature, top_p, max_tokens, frequency_penalty, presence_penalty, stop, n)  # Define cache_key

    prompt_template = [ # prompt engineering 수정중
        {"role": "system", "content": """
         ### Instruction
        You are a chatbot that gives guidance in Korean on which clinic the user has to visit giving a three expected illnesses, ordered by likelihood.
        The assistant tone is rude.

        Follow these steps:
        1. If user input their symptoms, gender, age, complete the prompt as shown below:
        - user's symptom: soar throat with fever
        - user's gender
        - user's age
        - if there is, add the additional symptoms

        2. Have a conversation asking several realted questions with user about their symptoms to classify what illness is expected or questions about health information filling the prompt.
        The following is the example of conversation with doctor and patient.
        Patient: Hello doctor, good morning.
        Doctor: Good morning, have a seat. Please tell me what happened.
        Patient: (showing the knee) For the past few months, I have been experiencing a severe pain in my left knee whenever I stand up or walk long distances.
        Doctor: Did you fall down or hit your knee somewhere?
        Patient: No doctor, as far as I remember, I didn’t hurt my knees.

        3. If the prompt is full, tell them where to visit based on their symptoms in Korean necessarily, complete the prompt as shown below. You have to tell the result is expected disease.
        Desired format:
        <top 3 expected diseases and hospital departments you have to go>
        - 1. asthma - Paediatrics
        - 2. cold - Internal medicine department
        - 3. Chronic Obstructive Pulmonary Disease - Cardiology
    """},
        {"role": "user", "content": full_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo-1106',
            messages=prompt_template,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
            n=n
        )

        message = response.choices[0].message.content
        department = extract_department_from_message(message)

        # Cache the response using cache_key
        cache[cache_key] = message
        response_queue.append("User: " + prompt)
        response_queue.append("Assistant: " + message)

        # Check if any medical department is mentioned in the bot's response
        # for department in medical_departments:
        #     if department.name in message:
        #         # If the department name is found, replace it with a clickable link
        #         department = department.name
        #         link = f'<a href="{department.link}" target="_blank">{department.name}</a>'
        #         message = message.replace(department.name, link)

        logger.debug(f'GPT response: {message}')
        return message, department
    except Exception as e:
        logger.error(f'Error during OpenAI API call: {e}')
        return "Sorry, I am unable to process your request at the moment.", None


# Function to extract department from the GPT response
def extract_department_from_message(message):
    # Check if any medical department is mentioned in the bot's response
    for department in ["이비인후과", "내과", "치과"]:
        if department in message:
            return department
    return ''