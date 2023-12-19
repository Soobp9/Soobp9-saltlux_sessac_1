# <main.py>
# uvicorn main:app --reload
import json
import openai
from fastapi import Query
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import ChatCompletion, OpenAI
from dotenv import load_dotenv
import logging
import os

# mongodb.py에서 함수 import
from mongo import insert_item_many, fetch_conversation_from_db
from summarization import summarize_conversation
from pinecone_utils import query_pinecone_with_metadata




# Simple in-memory cache
cache = {}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# OpenAI API key setup
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=API_KEY)

# Initialize OpenAI client
openai.api_key = os.getenv('OPENAI_API_KEY')
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
    # conversation_id: str  # Add a field for the conversation ID

class BotResponse(BaseModel):
    bot_message: str

class MedicalDepartment(BaseModel):
    name: str
    link: str

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

    logger.debug(f'Received POST request: {user_question}')

    if user_question:
        trim_conversation_history()
        response_queue.append({"role": "user", "content": user_question})

        # Generate the summary of the conversation
        conversation_summary = summarize_conversation(response_queue)

        # Query Pinecone with the summary (if necessary, depends on your application logic)
        pinecone_results = query_pinecone_with_metadata(conversation_summary)

        # Now use the conversation_summary and/or pinecone_results in your GPT query
        gpt_answer, department = get_qa_by_gpt(conversation_summary + " " + user_question)  # Modify this as per your need

        response_queue.append({"role": "assistant", "content": gpt_answer})
        insert_conversation_to_db()

        logger.debug(f'Response queue: {response_queue}')
        return JSONResponse(content={'bot_message': gpt_answer, 'department': department})
    else:
        return JSONResponse(content={'bot_message': 'No input received', 'department': ''})

# Additional endpoint to get the response
@app.get('/response/', response_class=JSONResponse)
async def get_response():
    if response_queue:
        return JSONResponse(content={'bot_message': response_queue.pop(0)})
    else:
        return JSONResponse(content={'bot_message': 'No response', 'department': ''})


# Function to get Q&A from GPT
def get_qa_by_gpt(prompt, temperature=0.3, top_p=0.5, max_tokens=600, frequency_penalty=0.3, presence_penalty=0.1, stop=None, n=1):
    # Include the conversation history in the prompt
    conversation_history = response_queue
    full_prompt = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation_history])

    cache_key = (prompt, temperature, top_p, max_tokens, frequency_penalty, presence_penalty, stop, n)  # Define cache_key

    prompt_template = [
    {"role": "system", "content": """I am a good and kind medical assistant.
         I will respond in Korean with answers of fewer than 70 words. If the user
         provides their symptoms, gender, and age, I will provide three likely
         medical conditions. When a user presents information about his or her symptoms,
         “다른 증상은 없나요?” is asked only once in the entire conversation and must
         be answered in the following format. "당신의 증상과 건강상태를 고려하면 유력한
         질병은 (질환명1) (0~100%), (질환명2) (0~100%), (질환명3) (0~100%) 일 가능성이
         높습니다냥. 이에 따라 당신이 방문해야 할 진료과를 추천드리면
         <질환명1과 관련한 진료과 목록>, <질환명2과 관련한 진료과 목록>,
         <질환명3과 관련한 진료과 목록>입니다."`
         (Considering your symptoms and health, the likely diseases
         are (Disease 1) (0~100%), (Disease 2) (0~100%), (Disease 3) (0~100%).
         Accordingly, I recommend visiting <Specialty 1>, <Specialty 2>,
         <Specialty 3>.) """},
        {"role": "user", "content": full_prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
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

        logger.debug(f'GPT response: {message}')
        return message, department
    except Exception as e:
        logger.error(f'Error during OpenAI API call: {e}')
        return "Sorry, I am unable to process your request at the moment.", None


# 진료과 필터
list_department = ["내과", "이비인후과", "정형외과", "신경과", "치과", "한의과", "정신과", "외과", "산부인과", "소아청소년과", "비뇨의학과", "응급의학과", "성형외과", "피부과", "안과", "가정의학과"]
def extract_department_from_message(message):
    # Check if any medical department is mentioned in the bot's response
    for department in list_department:
        if department in message:
            return department
    return ''


# MongoDB에 대화 넣기
def insert_conversation_to_db():
    if not response_queue[-1].get("inserted_to_db", False):
        inserted_id = insert_item_many(response_queue, db_name="Cluster17", collection_name='pique03')
        if inserted_id:
            response_queue[-1]["inserted_to_db"] = True
            logger.debug(f'Data inserted with ID: {inserted_id}')
        else:
            logger.error('Failed to insert data into MongoDB')

        
        
        
        
        
# # Additional endpoint to retrieve and process conversation from MongoDB
# @app.get('/process_conversation/', response_class=JSONResponse)
# async def process_conversation(conversation_id: str = Query(..., description="ID of the conversation in MongoDB")):
#     """
#     Retrieve and process a conversation from MongoDB based on the provided ID.

#     Parameters:
#         - conversation_id (str): ID of the conversation in MongoDB.

#     Returns:
#         - JSONResponse: Processed conversation with GPT answer and department information.
#     """

#     try:
#         # Fetch the conversation from MongoDB based on the provided ID
#         conversation = fetch_conversation_from_db(conversation_id)

#         if not conversation:
#             return JSONResponse(content={'bot_message': 'Conversation not found', 'department': ''})

#         # Process the conversation using the GPT model
#         gpt_answer, department = get_qa_by_gpt(conversation)

#         # Return the processed conversation
#         return JSONResponse(content={'bot_message': gpt_answer, 'department': department})
#     except Exception as e:
#         logger.error(f'Error processing conversation with ID {conversation_id}: {e}')
#         return JSONResponse(content={'bot_message': f'Error processing conversation with ID {conversation_id}', 'department': ''})