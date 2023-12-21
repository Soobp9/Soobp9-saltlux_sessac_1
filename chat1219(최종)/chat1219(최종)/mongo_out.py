# <mongo_out.py>
from pymongo import MongoClient

def get_latest_conversations(mongo_uri, db_name, collection_name, limit=5):
    client = MongoClient(MONGODB_URI)
    db = client[Cluster17]
    collection = db[pique03]

    try:
        latest_conversations = collection.find().sort("_id", -1).limit(limit)
        return list(latest_conversations)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        client.close()

