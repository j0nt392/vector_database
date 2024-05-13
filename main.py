import matplotlib.pyplot as plt
import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os
from Plotting import Plotting
from VectorDatabase import VectorDatabase
from CodeSummarizer import CodeSummarizer
from Embeddings import Embeddings
from utils import AST_parser
from CodeReview import CodeReview
import git
from decorators import measure_time, log_errors

# Set environment variable to avoid MKL errors
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

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
        self.Repo = git.Repo('/Users/jonte/kodprojekt/gunnar')

        self.route_command()

    def setup_parser(self):
        parser = argparse.ArgumentParser(description="CLI for interacting with AI models and codebase information")
        parser.add_argument("command", help="The command to run", choices=["query_vdb", "get_summary", "extract_and_embed", "code_review", "plot_vdb"])
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

    @log_errors
    def query_vdb(self):
        if not self.args.query:
            print("Error: --query parameter is required for 'query_vdb'")
            self.parser.print_help()
            return
        query_embedding = self.embeddings.create_code_embedding(self.args.query)
        print(query_embedding)
        query_embedding = query_embedding.squeeze()
        results = self.db.search(query_embedding)
        print("Search results:")
        for idx, result in results:
            print(f"\nResult {idx}:")
            print(f"File Path: {result['file_path']}")
            print(f"Start Line: {result['start_line']}, End Line: {result['end_line']}")
            print(f"Type: {result['type']}\n")
            print(f"Code Segment:\n {result['code_segment']}")
            print('-----------------------------------------')
        raise ValueError("This is a test error")

    @measure_time
    def get_summary(self):
        if not self.args.dir:
            print("Error: directory is required for 'get_summary'")
            self.parser.print_help()
            return
        summary = self.summarizer.process_directory(self.args.dir)
        print(summary)

    @log_errors
    def extract_and_embed(self):
        if not self.args.dir:
            print("Error: directory is required for 'extract_and_embed'")
            self.parser.print_help()
            return
        if not os.path.exists(self.args.dir):
            print(f"Error: The directory {self.args.dir} does not exist.")
            return
        
        code_extractor = AST_parser(self.args.dir)
        
        code_blocks = code_extractor.extract_code_blocks()
        for i, block in enumerate(code_blocks):
            print(f"Processing block {i+1}/{len(code_blocks)}...")
            embedding = self.embeddings.create_code_embedding(block['code_segment'])
            print(embedding.shape)
            embedding = embedding.squeeze() 
            self.db.add_embedding(embedding, block)


    @log_errors  
    def code_review(self):
        if not self.args.file:
            print("Error: file is required for 'code_review")
            self.parser.print_help()
            return
        if not os.path.exists(self.args.file):
            print(f"Error: The file {self.args.file} does not exist.")
            return
        
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
            
            # Commit changes to the repository
            self.Repo.git.add(self.args.file)
            self.Repo.git.commit(m=f"Optimized code in {self.args.file}")
            print("Changes committed to the repository.")
        
        else:
            print("No changes implemented.")
    
    @log_errors
    def plot_vdb(self):
        title = input("Enter the title of the plot: ")
        n_clusters = int(input("Enter the number of clusters: "))
        plotter = Plotting(self.db.get_all_vectors())
        plotter.plot_2D_cluster_pca(title, n_clusters)

if __name__ == "__main__":
    cli = CLI()
    
