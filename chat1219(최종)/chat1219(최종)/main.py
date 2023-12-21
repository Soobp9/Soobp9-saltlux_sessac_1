# <main.py>
# uvicorn main:app --reload

import openai
from fastapi import FastAPI
from typing import List
from mongo_out import get_latest_conversations
from mongo_in import save_conversation
from summarization import summarize_conversation

app = FastAPI()

MONGO_URI = "MONGO_URI"
DB_NAME = "Cluster17"
COLLECTION_NAME = "pique03"

@app.get("/process_conversations/{user_input}")
async def process_conversations(user_input: str):
    # Step 1: Retrieve the last five conversations
    last_five = get_latest_conversations(MONGO_URI, DB_NAME, COLLECTION_NAME)
    
    # Step 2 and 3: Summarize the conversations
    summa_five = summarize_conversation(last_five)

    # Step 4: Combine the summary with the full prompt
    full_prompt = f"Summary: {summa_five}"

    # Step 5: Get user input (already received as a parameter)

    # Step 6: Decide whether to use pinecone_utils.py
    fornext = user_input + " " + summa_five
    use_pinecone = should_use_pinecone(fornext)

    if use_pinecone:
        # Step 7-1: Use pinecone_utils.py functionality
        pinecone_results = pinecone_utils.query_pinecone(fornext)

        # Step 7-2 to 7-4: Handle metadata and form system response
        metadata = pinecone_results['metadata']  # Example extraction of metadata
        system_response = "Your system response based on metadata"
    else:
        # Step 8: Generate system response based on fornext
        system_response = get_qa_by_gpt(user_input, last_five, use_pinecone=False)

    # Step 9: Save the user-system conversation
    conversation = {"user_message": user_input, "system_response": system_response}
    save_conversation(MONGO_URI, DB_NAME, COLLECTION_NAME, conversation)

    return {"response": system_response}



# Function to get Q&A from GPT
def get_qa_by_gpt(user_input, response_queue, use_pinecone=False):
    temperature = 0.3
    top_p = 0.5
    max_tokens = 400
    frequency_penalty = 0.3
    presence_penalty = 0.1
    stop = None
    n = 1

    # Add user input to the conversation history
    response_queue.append({"role": "user", "content": user_input})
    full_prompt = "\n".join([f"{turn['role']}: {turn['content']}" for turn in response_queue])

    # Define the prompt template
    prompt_template = [
        {"role": "system", "content": "Your system prompt here..."},
        {"role": "user", "content": full_prompt}
    ]

    # Decide whether to use pinecone_utils.py based on criteria or keywords in user_input
    # For example, if 'diagnose' in user_input:
    if 'some_criteria' in user_input:
        use_pinecone = True

    try:
        # If use_pinecone is True, use pinecone_utils.py functionality
        if use_pinecone:
            # Call to pinecone_utils.py functionality here
            # For example:
            # message, department = pinecone_utils.query_pinecone(user_input, full_prompt)
            pass
        else:
            # Generate GPT response
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

        return message
    except Exception as e:
        logger.error(f'Error during OpenAI API call: {e}')
        return "Sorry, I am unable to process your request at the moment."

def should_use_pinecone(user_input):
    prompt = f"""
    Determine if the following user input requires using Pinecone for a detailed analysis. The criteria for using Pinecone are: [Define your specific criteria here]

    User Input: "{user_input}"

    Should Pinecone be used for a more detailed analysis? (Yes/No)
    """
    response = openai.Completion.create(
        model='gpt-3.5-turbo-1106',
        prompt=prompt,
        max_tokens=10
    )
    decision = response.choices[0].text.strip()
    return decision.lower() == 'yes'

# Example Usage
user_input = "Describe symptoms of common cold."
if should_use_pinecone(user_input):
    # Use pinecone_utils.py functionality
    pass
else:
    # Continue with regular processing
    pass

















# ==============================================================
# import json
# import openai
# from fastapi import Query
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from openai import ChatCompletion, OpenAI
# from dotenv import load_dotenv
# import logging
# import os

# # mongodb.py에서 함수 import
# from mongo import insert_item_many, fetch_conversation_from_db
# from summarization import summarize_conversation
# from pinecone_utils import query_pinecone_with_metadata




# # Simple in-memory cache
# cache = {}

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # OpenAI API key setup
# load_dotenv()
# API_KEY = os.environ['OPENAI_API_KEY']
# client = OpenAI(api_key=API_KEY)

# # Initialize OpenAI client
# openai.api_key = os.getenv('OPENAI_API_KEY')
# # FastAPI app setup
# app = FastAPI()

# # CORS setup
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # FastAPI models
# class UserRequest(BaseModel):
#     utterance: str
#     # conversation_id: str  # Add a field for the conversation ID

# class BotResponse(BaseModel):
#     bot_message: str

# class MedicalDepartment(BaseModel):
#     name: str
#     link: str

# # Queue object creation
# response_queue = []

# # Template directory setup
# templates = Jinja2Templates(directory="templates")

# # Maximum number of previous exchanges to keep
# MAX_HISTORY_LENGTH = 7

# # Function to trim the conversation history
# def trim_conversation_history():
#     global response_queue
#     if len(response_queue) > MAX_HISTORY_LENGTH:
#         # Keep only the last MAX_HISTORY_LENGTH exchanges
#         response_queue = response_queue[-MAX_HISTORY_LENGTH:]

# # Root endpoint for rendering HTML
# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# # Chatbot endpoint
# @app.post('/chatbot/', response_model=BotResponse)
# async def chat(user_request: UserRequest):
#     user_question = user_request.utterance.strip()

#     logger.debug(f'Received POST request: {user_question}')

#     if user_question:
#         trim_conversation_history()
#         response_queue.append({"role": "user", "content": user_question})

#         # Generate the summary of the conversation
#         conversation_summary = summarize_conversation(response_queue)

#         # Query Pinecone with the summary (if necessary, depends on your application logic)
#         pinecone_results = query_pinecone_with_metadata(conversation_summary)

#         # Now use the conversation_summary and/or pinecone_results in your GPT query
#         gpt_answer, department = get_qa_by_gpt(conversation_summary + " " + user_question)  # Modify this as per your need

#         response_queue.append({"role": "assistant", "content": gpt_answer})
#         insert_conversation_to_db()

#         logger.debug(f'Response queue: {response_queue}')
#         return JSONResponse(content={'bot_message': gpt_answer, 'department': department})
#     else:
#         return JSONResponse(content={'bot_message': 'No input received', 'department': ''})

# # Additional endpoint to get the response
# @app.get('/response/', response_class=JSONResponse)
# async def get_response():
#     if response_queue:
#         return JSONResponse(content={'bot_message': response_queue.pop(0)})
#     else:
#         return JSONResponse(content={'bot_message': 'No response', 'department': ''})


# # Function to get Q&A from GPT
# def get_qa_by_gpt(prompt, temperature=0.3, top_p=0.5, max_tokens=600, frequency_penalty=0.3, presence_penalty=0.1, stop=None, n=1):
#     # Include the conversation history in the prompt
#     conversation_history = response_queue
#     full_prompt = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation_history])

#     cache_key = (prompt, temperature, top_p, max_tokens, frequency_penalty, presence_penalty, stop, n)  # Define cache_key

#     prompt_template = [
#     {"role": "system", "content": """I am a good and kind medical assistant.
#          I will respond in Korean with answers of fewer than 70 words. If the user
#          provides their symptoms, gender, and age, I will provide three likely
#          medical conditions. When a user presents information about his or her symptoms,
#          “다른 증상은 없나요?” is asked only once in the entire conversation and must
#          be answered in the following format. "당신의 증상과 건강상태를 고려하면 유력한
#          질병은 (질환명1) (0~100%), (질환명2) (0~100%), (질환명3) (0~100%) 일 가능성이
#          높습니다냥. 이에 따라 당신이 방문해야 할 진료과를 추천드리면
#          <질환명1과 관련한 진료과 목록>, <질환명2과 관련한 진료과 목록>,
#          <질환명3과 관련한 진료과 목록>입니다."`
#          (Considering your symptoms and health, the likely diseases
#          are (Disease 1) (0~100%), (Disease 2) (0~100%), (Disease 3) (0~100%).
#          Accordingly, I recommend visiting <Specialty 1>, <Specialty 2>,
#          <Specialty 3>.) """},
#         {"role": "user", "content": full_prompt}
#     ]

#     try:
#         response = openai.ChatCompletion.create(
#             model='gpt-3.5-turbo-1106',
#             messages=prompt_template,
#             temperature=temperature,
#             top_p=top_p,
#             max_tokens=max_tokens,
#             frequency_penalty=frequency_penalty,
#             presence_penalty=presence_penalty,
#             stop=stop,
#             n=n
#         )

#         message = response.choices[0].message.content
#         department = extract_department_from_message(message)

#         logger.debug(f'GPT response: {message}')
#         return message, department
#     except Exception as e:
#         logger.error(f'Error during OpenAI API call: {e}')
#         return "Sorry, I am unable to process your request at the moment.", None


# # MongoDB에 대화 넣기
# def insert_conversation_to_db():
#     if not response_queue[-1].get("inserted_to_db", False):
#         inserted_id = insert_item_many(response_queue, db_name="Cluster17", collection_name='pique03')
#         if inserted_id:
#             response_queue[-1]["inserted_to_db"] = True
#             logger.debug(f'Data inserted with ID: {inserted_id}')
#         else:
#             logger.error('Failed to insert data into MongoDB')

        
        
        
