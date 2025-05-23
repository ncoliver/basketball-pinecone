import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

index_name = "quickstart"

index = pc.Index("quickstart")

