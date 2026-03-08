import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        print("Initializing FAISS index...")

        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

        print("Vector database ready")

    def add_documents(self, embeddings, documents):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.documents.extend(documents)

        print("Documents added to vector database:", len(documents))

    def search(self, query_embedding, k=5):

        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i in indices[0]:
            results.append(self.documents[i])

        return results