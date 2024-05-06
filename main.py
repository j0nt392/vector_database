from Embeddings import Embeddings
from VectorDatabase import VectorDatabase
from utils import CodeExtractor
from CodeSummarizer import CodeSummarizer
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)  # Singleton OpenAI client

def main():
    summarizer = CodeSummarizer(client)
    directory_path = 'test_repository'
    summaries = summarizer.process_directory(directory_path)    
    print(summaries)
    # db = VectorDatabase()
    # emb = Embeddings(client)
    # extractor = CodeExtractor('test_repository')

    # blocks = extractor.extract_code_blocks()
    # for block in blocks:
    #     embedding = emb.create_code_embedding(block['code_segment'])
    #     # Include code segment in the metadata
    #     metadata = {
    #         'file_path': block['file_path'],
    #         'line_info': f"Line {block['start_line']} - {block['end_line']}",
    #         'code_segment': block['code_segment']  # Store the actual code segment
    #     }
    #     db.add_embedding(embedding, metadata)
    
    # query_embedding = emb.create_code_embedding("Vector")
    # results = db.search(query_embedding, 5)
    # for idx, meta in results:
    #     print(f"Index {idx}: {meta['file_path']}, {meta['line_info']}")
    #     print(f"Code:\n{meta['code_segment']}")

if __name__ == "__main__":
    main()
