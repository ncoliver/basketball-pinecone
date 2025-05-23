from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key)

index_name = "quickstart"

pc.create_index(
    name=index_name,
    dimension=1024, # Replace with your model dimensions
    metric="euclidean", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)