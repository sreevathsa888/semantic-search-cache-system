import numpy as np
import skfuzzy as fuzz


class FuzzyCluster:

    def __init__(self, n_clusters=8):

        print("Initializing Fuzzy Clustering...")

        self.n_clusters = n_clusters
        self.centers = None
        self.membership = None

    def fit(self, embeddings):

        print("Running Fuzzy C-Means clustering...")

        data = np.array(embeddings).T

        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
            data,
            c=self.n_clusters,
            m=2,
            error=0.005,
            maxiter=1000,
            init=None
        )

        self.centers = cntr
        self.membership = u

        print("Clustering completed")

        return u

    def get_cluster_for_doc(self, doc_index):

        membership_scores = self.membership[:, doc_index]

        cluster = np.argmax(membership_scores)

        return cluster