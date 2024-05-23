from openai import OpenAI
import ollama 

class SearchReview:
    def __init__(self, client):
        self.client = client
    
    def Review_Results(self, results, query):
        
        prompt = f"Out of these results \n {results}, which one matches the best with the query: {query}?"
        prompt2 = f"this is the query from the user: {query} \n and these are the results: {results}"

        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt = prompt2,
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].text.strip() 

    def Review_Results_Ollama(self, results, query):
        prompt = f"Out of these results {results}, which one matches the best with the query: {query}? Reply with the index of the element in the list, no prefacing or trailing text."
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
            ])
        correct_index = int(response['message']['content'])
        return results[correct_index]