from embeddings import Embeddings
from VectorDatabase import VectorDatabase
from utils import CodeExtractor
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)  # Singleton OpenAI client

def main():
    db = VectorDatabase()
    emb = Embeddings(client)
    extractor = CodeExtractor('test_repository')

    blocks = extractor.extract_code_blocks()
    for block in blocks:
        embedding = emb.create_code_embedding(block['code_segment'])
        db.add_embedding(embedding)
    
    query_embedding = emb.create_code_embedding("def divide(a, b): return a / b")
    print(db.search(query_embedding, 5))


if __name__ == "__main__":
    main()