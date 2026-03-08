
from data.load_data import load_dataset
from embeddings.embedding_model import EmbeddingModel
from vectordb.vector_store import VectorStore
from cache.semantic_cache import SemanticCache


print("Loading dataset...")
documents = load_dataset()

embedder = EmbeddingModel()

doc_embeddings = embedder.encode_documents(documents[:2000])

dimension = len(doc_embeddings[0])

vector_db = VectorStore(dimension)

vector_db.add_documents(doc_embeddings, documents[:2000])

cache = SemanticCache(threshold=0.85)


queries = [
    "space exploration and nasa missions",
    "satellite launches in space",
    "baseball world series",
    "space shuttle mission"
]


for q in queries:

    print("\nQuery:", q)

    q_embedding = embedder.encode_query(q)

    cached_result, hit = cache.check_cache(q_embedding)

    if hit:
        print("Returned from cache")
        continue

    results = vector_db.search(q_embedding)

    cache.add_to_cache(q, q_embedding, results)

    print("Search executed and stored in cache")


print("\nCache Stats:")

print(cache.stats())