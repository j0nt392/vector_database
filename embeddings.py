import numpy as np
from transformers import AutoModel, AutoTokenizer


class Embeddings:
    """
    Class to handle embeddings for code snippets using the Microsoft CodeBERT model.
    
    Attributes:
        model: Pretrained CodeBERT model.
        tokenizer: Pretrained CodeBERT tokenizer.
        client: OpenAI API client (optional).
    """
    def __init__(self, client=None):
        """
        Initializes the Embeddings class.
        
        Args:
            client (optional): OpenAI API client.
        """
        self.client = client
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

    def create_code_embedding(self, code_snippet):
        """
        Creates a code embedding using the CodeBERT model.

        Args:
            code_snippet: Code snippet to be embedded.
            
        Returns:
            An L2-normalized embedding vector for the code snippet.
        """
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
        """
        Normalizes the input vector using L2 normalization.

        Args:
            normalized_x: Vector to be normalized.

        Returns:
            The normalized vector.
        """
        normalized_x = np.array(normalized_x)
        if normalized_x.ndim == 1:
            norm = np.linalg.norm(normalized_x)
            if norm == 0:
                return normalized_x
            return normalized_x / norm
        else:
            norm = np.linalg.norm(normalized_x, 2, axis=1, keepdims=True)
            return np.where(norm == 0, normalized_x, normalized_x / norm)