import os
import numpy as np

class Embeddings:
    def __init__(self, client):
        self.client = client

    def create_code_embedding(self, code):
        response = self.client.embeddings.create(
            model="text-embedding-3-small", 
            input=code, 
            encoding_format="float"
        )
        cut_dim = response.data[0].embedding[:256]
        return self._normalize_l2(cut_dim)

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







