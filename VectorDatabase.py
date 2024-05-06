import faiss
import numpy as np

class VectorDatabase:
    def __init__(self):
        self.index = faiss.IndexFlatL2(256)  # Dimension of the embeddings

    def add_embedding(self, embedding):
        if embedding is not None:
            self.index.add(np.array([embedding], dtype='float32'))

    def search(self, query_embedding, k=5):
        D, I = self.index.search(np.array([query_embedding], dtype='float32'), k)
        return I[0]
