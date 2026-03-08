from data.load_data import load_dataset
from embeddings.embedding_model import EmbeddingModel


print("Loading dataset...")

documents = load_dataset()

print("Total documents:", len(documents))


embedder = EmbeddingModel()

# Only first 1000 docs for testing
embeddings = embedder.encode_documents(documents[:1000])


print("Embeddings generated:", len(embeddings))

print("Embedding dimension:", len(embeddings[0]))