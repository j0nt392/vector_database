from openai import OpenAI
import ollama
from decorators import log_errors

class CodeReview:
    def __init__(self, client):
        self.client = client

    def get_code(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            return content
        
    @log_errors
    def get_code_suggestion(self, code, change_type):
        prompt = self._generate_prompt(code, change_type)        
        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt = prompt,
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].text.strip()

            
    def implement_changes(self, code, suggestion):
        prompt = f"### Rewrite the entire code with the changes implemented:\n{suggestion}\n in the code: {code}.\n"
        try:
            # response = self.client.completions.create(
            #     model="gpt-3.5-turbo-instruct",
            #     prompt = prompt,
            #     max_tokens=1000,
            #     temperature=0.7
            # )
            # return response.choices[0].text.strip()
            response = ollama.chat(model='llama3', messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
                ])
            return response['message']['content']
        except Exception as e:
            print(f"Error implementing changes: {e}")
            return None
    
    def _generate_prompt(self, code, change_type):
        return f"### You will suggest changes to this code:\n{code}\n### You will suggest modifications of type: {change_type}\n"
