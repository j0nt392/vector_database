import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os
from VectorDatabase import VectorDatabase
from CodeSummarizer import CodeSummarizer
from Embeddings import Embeddings
from utils import AST_parser
from CodeReview import CodeReview

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
        self.code_reviewer = CodeReview(client)
        self.route_command()

    def setup_parser(self):
        parser = argparse.ArgumentParser(description="CLI for interacting with AI models and codebase information")
        parser.add_argument("command", help="The command to run", choices=["query_vdb", "get_summary", "extract_and_embed", "code_review"])
        parser.add_argument("--dir", help="Directory to process for extracting and embedding code blocks")
        parser.add_argument("--file", help="File to review code")
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
        if not self.args.dir:
            print("Error: directory is required for 'get_summary'")
            self.parser.print_help()
            return
        summary = self.summarizer.process_directory(self.args.dir)
        print(summary)

    def extract_and_embed(self):
        if not self.args.dir:
            print("Error: directory is required for 'extract_and_embed'")
            self.parser.print_help()
            return
        if not os.path.exists(self.args.dir):
            print(f"Error: The directory {self.args.dir} does not exist.")
            return
        
        code_extractor = AST_parser(self.args.dir)
        try:
            code_blocks = code_extractor.extract_code_blocks()
            for i, block in enumerate(code_blocks):
                print(f"Processing block {i+1}/{len(code_blocks)}...")
                embedding = self.embeddings.create_code_embedding(block['code_segment'])
                self.db.add_embedding(embedding, block)
        except Exception as e:
            print(f"Failed to process directory: {e}")
        
    def code_review(self):
        if not self.args.file:
            print("Error: file is required for 'code_review")
            self.parser.print_help()
            return
        if not os.path.exists(self.args.file):
            print(f"Error: The file {self.args.file} does not exist.")
            return
        try:
            code = self.code_reviewer.get_code(self.args.file)
            optimization_type= input("What modification type do you want to suggest? Press Enter to continue...")
            review = self.code_reviewer.get_code_suggestion(code, optimization_type)
            print(review)
            user_response = input("Implement suggested changes? y/n:")
            if user_response.lower() == 'y':
                print("implementing changes...")
                new_code = self.code_reviewer.implement_changes(code, review)
                print(new_code)
                with open(self.args.file, 'w') as f:
                    f.write(new_code)
                print("Changes implemented successfully.")
            else:
                print("No changes implemented.")

        except Exception as e:
            print(f"Failed to review code: {e}")

if __name__ == "__main__":
    cli = CLI()
    

    # Without using classes:

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

