from openai import OpenAI
import os 
from dotenv import load_dotenv 
import numpy as np

load_dotenv()

class Embeddings:
    def __init__(self):
        openai_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=openai_key)

    def get_embedding(self, code):
        response = self.client.embeddings.create(
            model="text-embedding-3-small", 
            input=code, 
            encoding_format="float"
        )
        cut_dim = response.data[0].embedding[:256]
        norm_dim = self._normalize_l2(cut_dim)
        return norm_dim

    def _normalize_l2(self, x):
        x = np.array(x)
        if x.ndim == 1:
            norm = np.linalg.norm(x)
            if norm == 0:
                return x
            return x / norm
        else:
            norm = np.linalg.norm(x, 2, axis=1, keepdims=True)
            return np.where(norm == 0, x, x  / norm)

# Usage
embedding = Embeddings()
print(embedding.get_embedding("def add(a, b): return a + b"))
