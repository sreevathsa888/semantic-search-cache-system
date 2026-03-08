from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Model loaded successfully")

    def encode_documents(self, documents):

        print("Generating embeddings for documents...")

        embeddings = self.model.encode(
            documents,
            show_progress_bar=True
        )

        return embeddings

    def encode_query(self, query):

        embedding = self.model.encode([query])

        return embedding