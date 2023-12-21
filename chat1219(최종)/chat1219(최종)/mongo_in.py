# <mongo_in.py>
from pymongo import MongoClient
import datetime

def save_conversation(MONGODB_URI, db_name, collection_name, conversation):
    client = MongoClient(MONGODB_URI)
    db = client[Cluster17]
    collection = db[pique03]

    try:
        inserted_id = collection.insert_one(conversation).inserted_id
        return inserted_id
    except Exception as e:
        print(f"An error occurred while saving the conversation: {e}")
        return None
    finally:
        client.close()



# ===================================
# def save_conversation(mongo_uri, db_name, collection_name, user_message, system_response):
#     # Connect to the MongoDB client
#     client = MongoClient(mongo_uri)

#     # Select the database and collection
#     db = client[db_name]
#     collection = db[collection_name]

#     # Conversation document
#     conversation = {
#         "user_message": user_message,
#         "system_response": system_response,
#         "timestamp": datetime.datetime.utcnow()
#     }

#     try:
#         # Insert the document into the collection
#         inserted_id = collection.insert_one(conversation).inserted_id
#         print(f"Conversation saved with ID: {inserted_id}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the connection to MongoDB
#         client.close()

# # Usage example
# mongo_uri = "your_mongodb_uri"
# db_name = "your_database"
# collection_name = "your_collection"

# # Example conversation data
# user_message = "Hello, how are you?"
# system_response = "I'm an AI, so I don't have feelings, but I'm here to help you!"

# save_conversation(mongo_uri, db_name, collection_name, user_message, system_response)



# =====================================
# import os
# from fastapi import Query
# from pymongo import MongoClient
# from datetime import *
# from bson import ObjectId
# from dotenv import load_dotenv


# load_dotenv()
# MONGODB_URI = os.environ['MONGODB_URI']
# host = "localhost"
# port = "27017"
# client = MongoClient(MONGODB_URI)



# def insert_item_many(data, db_name = None, collection_name = None):
#     db = client[db_name]
#     collection = db[collection_name]

#     # response_queue가 비어있는 경우 처리
#     if not data:
#         return None
#     # 여기서 response_queue를 딕셔너리 형태로 감싸서 처리
#     try:
#         # 여기서 response_queue를 딕셔너리 형태로 감싸서 처리
#         documents = [
#             {"timestamp": datetime.now(), "Response queue": [{"role": item["role"], "content": item["content"]} for item in data]}
#         ]
#         result = collection.insert_many(documents)
#         inserted_ids = result.inserted_ids
#         return inserted_ids
#     except Exception as e:
#         print(f"Error inserting data into MongoDB: {e}")
#         return None


# def fetch_conversation_from_db(conversation_id):
#     client = MongoClient('MONGODB_URI')
#     db = client["Cluster17"]
#     collection = db["pique03"]

#     # Convert the string representation of ObjectId back to ObjectId
#     conversation_id = ObjectId(conversation_id)

#     # Fetch the conversation based on the specified "_id"
#     conversation_document = collection.find_one({"_id": conversation_id})

#     # Log the conversation document for debugging
#     print(f"Conversation document: {conversation_document}")

#     if conversation_document:
#         # Extract the conversation content from the document
#         conversation = conversation_document.get("Response queue")

#         # Log the conversation content for debugging
#         print(f"Conversation content: {conversation}")

#         return conversation
#     else:
#         print(f"Conversation not found for ID: {conversation_id}")
#         return None