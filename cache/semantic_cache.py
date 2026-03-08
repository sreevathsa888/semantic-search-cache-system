import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCache:

    def __init__(self, threshold=0.85):

        print("Initializing semantic cache...")

        self.cache = []
        self.threshold = threshold

        self.hit_count = 0
        self.miss_count = 0

    def check_cache(self, query_embedding):

        for entry in self.cache:

            similarity = cosine_similarity(
                query_embedding,
                entry["embedding"]
            )[0][0]

            if similarity > self.threshold:

                self.hit_count += 1

                print("Cache hit!")

                return entry["result"], True

        self.miss_count += 1

        print("Cache miss!")

        return None, False

    def add_to_cache(self, query, embedding, result):

        self.cache.append({
            "query": query,
            "embedding": embedding,
            "result": result
        })

    def stats(self):

        total = self.hit_count + self.miss_count

        hit_rate = self.hit_count / total if total else 0

        return {
            "total_entries": len(self.cache),
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }

    def clear(self):

        self.cache = []

        self.hit_count = 0
        self.miss_count = 0