import faiss
import numpy as np

class VectorDatabase:
    def __init__(self):
        self.index = faiss.IndexFlatL2(256)  # Dimension of the embeddings
        self.metadata = []  # Expanded to include code segments

    def add_embedding(self, embedding, metadata):
        if embedding is not None:
            self.index.add(np.array([embedding], dtype='float32'))
            self.metadata.append(metadata)  # Metadata now includes the code segment

    def search(self, query_embedding, k=5):
        D, I = self.index.search(np.array([query_embedding], dtype='float32'), k)
        return [(i, self.metadata[i]) for i in I[0]] 