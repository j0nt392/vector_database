import os
from openai import OpenAI
import json

class CodeSummarizer:
    def __init__(self, client):
        self.client = client
    
    def _summarize_file(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        prompt = f"Provide a brief summary of this Python code in one or two sentences:\n\n{content}\n\n### End of Code ###"
        summary = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100,
            temperature=0.5
        )
        return summary.choices[0].text.strip()
    
    def process_directory(self, directory_path):
        summaries = {}
        for filename in os.listdir(directory_path):
            if filename.endswith('.py'):
                file_path = os.path.join(directory_path, filename)
                summaries[file_path] = self._summarize_file(file_path)
        self._save_summaries_to_json(summaries, 'summaries.json')
        return summaries
    
    def _save_summaries_to_json(self, summaries, output_path):
        with open(output_path, 'w') as f:
            json.dump(summaries, f, indent=4)
            print(f"saving summaries to {output_path}...")

