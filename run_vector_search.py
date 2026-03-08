from data.load_data import load_dataset
from embeddings.embedding_model import EmbeddingModel
from vectordb.vector_store import VectorStore


print("Loading dataset...")
documents = load_dataset()

print("Total documents:", len(documents))


embedder = EmbeddingModel()

print("Generating embeddings for documents...")
doc_embeddings = embedder.encode_documents(documents[:2000])


dimension = len(doc_embeddings[0])

vector_db = VectorStore(dimension)

vector_db.add_documents(doc_embeddings, documents[:2000])


query = "space exploration and nasa missions"

print("\nSearching for:", query)

query_embedding = embedder.encode_query(query)

results = vector_db.search(query_embedding, k=5)


print("\nTop Results:\n")

for i, doc in enumerate(results):
    print("Result", i + 1)
    print(doc[:300])
    print("\n-----------------\n")