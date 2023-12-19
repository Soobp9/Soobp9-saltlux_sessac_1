# <pinecone.py>

import os
import logging
import sys
import llama_index
import openai
import pinecone_utils
from transformers import AutoTokenizer, AutoModel
import torch
from llama_index.vector_stores import PineconeVectorStore
from decouple import config 
from dotenv import load_dotenv



load_dotenv()

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Retrieve API keys (Modify this part if not running on Google Colab)
# For VSCode or other IDEs, consider using environment variables or a secure method for handling API keys
api_key = config('PINECONE_API_KEY')
openai_api_key = config('OPENAI_API_KEY')

# Check versions of llama_index and openai
llama_index_version, openai_version = llama_index.__version__, openai.__version__
print(f"Llama Index version: {llama_index_version}, OpenAI version: {openai_version}")

# Pinecone setup
environment = "gcp-starter"
index_name = "health-dhver"  # Input your index name

pinecone_utils.init(api_key=api_key, environment=environment)
pinecone_index = pinecone_utils.Index(index_name)

# Initialize the tokenizer and model for embedding
model_name = "intfloat/multilingual-e5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to create embeddings
def create_embeddings(text, tokenizer, model):
    encoded_input = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        model_output = model(**encoded_input)
    embeddings = model_output.last_hidden_state.mean(dim=1).numpy()
    return embeddings

# Function to query Pinecone index with new embeddings and namespace, including metadata
def query_pinecone_with_metadata(text, namespace, pinecone_index, tokenizer, model):
    embeddings = create_embeddings(text, tokenizer, model)
    query_results = pinecone_index.query(embeddings.tolist(), top_k=5, namespace=namespace, include_metadata=True)
    return query_results

# Example usage
pinecone_index = pinecone_utils.Index("health-dhver")  # Replace with your index name
tokenizer = AutoTokenizer.from_pretrained("intfloat/multilingual-e5-large")  # Replace with your model name
model = AutoModel.from_pretrained("intfloat/multilingual-e5-large")  # Replace with your model name

def query_pinecone(summary):
    # Assuming 'summary' is the variable that contains the summary of the conversation
    return query_pinecone_with_metadata(summary, 'messispace', pinecone_index, tokenizer, model)

