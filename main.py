import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os

# Import your custom classes
from VectorDatabase import VectorDatabase
from CodeSummarizer import CodeSummarizer
from Embeddings import Embeddings
from utils import CodeExtractor

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)  # Singleton OpenAI client

class CLI:
    def __init__(self):
        self.parser = self.setup_parser()
        self.args = self.parser.parse_args()
        self.db = VectorDatabase(storage_path='path_to_your_saved_index')  # Modify as needed
        self.embeddings = Embeddings(client)
        self.summarizer = CodeSummarizer(client)
        self.route_command()

    def setup_parser(self):
        parser = argparse.ArgumentParser(description="CLI for interacting with AI models and codebase information")
        parser.add_argument("command", help="The command to run", choices=["query_vdb", "get_summary", "extract_and_embed"])
        parser.add_argument("directory", help="Directory to process for extracting and embedding code blocks", nargs="?")
        parser.add_argument("--query", help="Query string to search for", required=False)
        return parser

    def route_command(self):
        command_method = getattr(self, self.args.command, None)
        if command_method:
            command_method()
        else:
            print("Unknown command")
            self.parser.print_help()

    def query_vdb(self):
        if not self.args.query:
            print("Error: --query parameter is required for 'query_vdb'")
            self.parser.print_help()
            return
        try:
            query_embedding = self.embeddings.create_code_embedding(self.args.query)
            results = self.db.search(query_embedding)
            print("Search results:")
            for result in results:
                print(result)
        except Exception as e:
            print(f"Error processing query: {e}")


    def get_summary(self):
        if not self.args.directory:
            print("Error: directory is required for 'get_summary'")
            self.parser.print_help()
            return
        summary = self.summarizer.summarize_file(self.args.directory)
        print(summary)

    def extract_and_embed(self):
        if not self.args.directory:
            print("Error: directory is required for 'extract_and_embed'")
            self.parser.print_help()
            return
        if not os.path.exists(self.args.directory):
            print(f"Error: The directory {self.args.directory} does not exist.")
            return
        
        code_extractor = CodeExtractor(self.args.directory)
        try:
            code_blocks = code_extractor.extract_code_blocks()
            for i, block in enumerate(code_blocks):
                print(f"Processing block {i+1}/{len(code_blocks)}...")
                embedding = self.embeddings.create_code_embedding(block['code_segment'])
                self.db.add_embedding(embedding, block)
        except Exception as e:
            print(f"Failed to process directory: {e}")


if __name__ == "__main__":
    cli = CLI()
    
    # db = VectorDatabase()

    # # Attempt to load existing database
    # db.load_index('path_to_your_saved_index')  # You need to specify the path where your index and metadata will be saved

    # emb = Embeddings(client)
    # extractor = CodeExtractor('test_repository')

    # blocks = extractor.extract_code_blocks()
    # for block in blocks:
    #     embedding = emb.create_code_embedding(block['code_segment'])
    #     metadata = {
    #         'file_path': block['file_path'],
    #         'line_info': f"Line {block['start_line']} - {block['end_line']}",
    #         'code_segment': block['code_segment']  # Store the actual code segment
    #     }
    #     db.add_embedding(embedding, metadata)

    # # Save the database after processing all blocks
    # db.save_index('path_to_your_saved_index')  # Same path as the load to ensure consistency

    # # Later or in another session, you can perform searches
    # query_embedding = emb.create_code_embedding("Vector")
    # results = db.search(query_embedding, 5)
    # for idx, meta in results:
    #     print(f"Index {idx}: {meta['file_path']}, {meta['line_info']}")
    #     print(f"Code:\n{meta['code_segment']}")

