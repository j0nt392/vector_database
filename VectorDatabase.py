import faiss
import numpy as np
import pickle

class VectorDatabase:
    def __init__(self, storage_path='path_to_your_saved_index'):
        self.index_path = f"{storage_path}.index"
        self.metadata_path = f"{storage_path}.metadata"
        self.load_index()

    def add_embedding(self, embedding, metadata):
        if embedding is not None and np.any(embedding):  
            self.index.add(np.array([embedding], dtype='float32'))
            self.metadata.append(metadata)  
            self.save_index()  # Save after each update
        else:
            print("Invalid or empty embedding provided, not added to the index.")
    
    def search(self, query_embedding, k=1):
        """Search for the k nearest neighbors of the query_embedding."""
        try:
            print(query_embedding)
            D, I = self.index.search(np.array([query_embedding], dtype='float32'), k)
            print(I[0])
            return [(i, self.metadata[i]) for i in I[0]]  # Return indices and metadata
        except Exception as e:
            print(f"Search error: {e}")
            return []  # Return an empty list if there's an error

    def save_index(self):
        """Save the FAISS index and metadata to disk."""
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, 'wb') as f:
            pickle.dump(self.metadata, f)

    def load_index(self):
        """Load the FAISS index and metadata from disk."""
        try:
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, 'rb') as f:
                self.metadata = pickle.load(f)
        except FileNotFoundError:
            print(f"No saved index or metadata found, initializing new index.")
            self.index = faiss.IndexFlatL2(256)
            self.metadata = []
        except Exception as e:
            print(f"Failed to load index and metadata: {e}")
            self.index = faiss.IndexFlatL2(256)
            self.metadata = []
