from openai import OpenAI
import ollama
from decorators import log_errors

class CodeReview:
    def __init__(self, client):
        self.client = client
        
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
        prompt = f"### Rewrite the entire code with the changes implemented:\n{suggestion}\n in the code:\n"
        try:
            for codeblock in code:
                prompt += f"\n{codeblock['code_segment']}\n"  

            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt = prompt,
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].text.strip()

            # response = ollama.chat(model='llama3', messages=[
            #     {
            #         'role': 'user',
            #         'content': prompt,
            #     },
            #     ])
            # return response['message']['content']
        except Exception as e:
            print(f"Error implementing changes: {e}")
            return None
    
    def _generate_prompt(self, code, change_type):
        print(code)
        prompt = f"### Review the codeblocks given, and suggest changes based on:\n{change_type}\n Here is the code:\n"
        for codeblock in code:
            prompt += f"\n{codeblock}\n"  
        return prompt
    
    def get_code(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            return content