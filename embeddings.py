import numpy as np
from transformers import AutoModel, AutoTokenizer


class Embeddings:
    def __init__(self, client=None):
        self.client = client
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

    def create_code_embedding(self, code_snippet):
        # code_tokens = self.tokenizer.encode(code_snippet, return_tensors="pt", padding=True, truncation=True, max_length=128)
        # output = self.model(input_ids=code_tokens)
        # embedding = output.last_hidden_state.mean(dim=1).detach().numpy()
        # return self._normalize_l2(embedding) if np.any(embedding) else np.zeros(768)

        response = self.client.embeddings.create(
            model="text-embedding-3-small", 
            input=code_snippet, 
            encoding_format="float"
        )
        embedding = np.array(response.data[0].embedding[:768]) if response.data else np.zeros(768)
        return self._normalize_l2(embedding) if np.any(embedding) else np.zeros(768)

    def _normalize_l2(self, normalized_x):
        normalized_x = np.array(normalized_x)
        if normalized_x.ndim == 1:
            norm = np.linalg.norm(normalized_x)
            if norm == 0:
                return normalized_x
            return normalized_x / norm
        else:
            norm = np.linalg.norm(normalized_x, 2, axis=1, keepdims=True)
            return np.where(norm == 0, normalized_x, normalized_x / norm)