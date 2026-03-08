from data.load_data import load_dataset
from embeddings.embedding_model import EmbeddingModel
from clustering.fuzzy_cluster import FuzzyCluster


print("Loading dataset...")

documents = load_dataset()

print("Total documents:", len(documents))


embedder = EmbeddingModel()

print("Generating embeddings...")

embeddings = embedder.encode_documents(documents[:1500])


clusterer = FuzzyCluster(n_clusters=8)

membership = clusterer.fit(embeddings)


print("\nCluster assignment for first 10 documents:\n")

for i in range(10):

    cluster = clusterer.get_cluster_for_doc(i)

    print(f"Document {i} → Cluster {cluster}")