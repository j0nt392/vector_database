import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

class Plotting:
    def __init__(self, vector_database):
        self.vector_database = vector_database

    def plot_pca(self, title):
        """Plot a 2D scatter plot of the vectors using PCA."""
        if len(self.vector_database) < 2:
            print("Not enough data points to perform PCA.")
            return

        # Applying PCA to reduce dimensions to 2
        pca = PCA(n_components=2)
        vectors_2D = pca.fit_transform(self.vector_database)

        # Plotting the results
        plt.figure(figsize=(8, 6))
        plt.scatter(vectors_2D[:, 0], vectors_2D[:, 1], alpha=0.7)
        plt.title(title)
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.grid(True)
        plt.show()

    def plot_2D_cluster_pca(self, title, n_clusters):
        """Plot a 2D scatter plot of the vectors with clustering using PCA."""
        if len(self.vector_database) < 2:
            print("Not enough data points to perform PCA.")
            return

        # Applying PCA to reduce dimensions to 2
        pca = PCA(n_components=2)
        vectors_2D = pca.fit_transform(self.vector_database)

        # Clustering the reduced data
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(vectors_2D)
        cluster_labels = kmeans.labels_
        cluster_centers = kmeans.cluster_centers_

        # Plotting the results
        plt.figure(figsize=(8, 6))
        plt.scatter(vectors_2D[:, 0], vectors_2D[:, 1], c=cluster_labels, alpha=0.7, cmap='viridis')
        plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, alpha=0.5)  # Plot centers
        plt.title(title)
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.grid(True)
        plt.show()

    def plot_2D(self, title):
        # Convert the vectors to 2D using t-SNE
        tsne = TSNE(n_components=2, random_state=0)
        vectors_2D = tsne.fit_transform(self.vector_database)
        plt.scatter(vectors_2D[:, 0], vectors_2D[:, 1])
        plt.title(title)
        plt.show()

    def plot_2D_cluster(self, title, n_clusters):
        # Cluster the vectors
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(self.vector_database)
        cluster_labels = kmeans.labels_

        # Convert the vectors to 2D using t-SNE
        tsne = TSNE(n_components=2, random_state=0, perplexity=min(30, len(self.vector_database)-1))
        vectors_2D = tsne.fit_transform(self.vector_database)

        # Convert cluster centers to 2D using the same t-SNE model
        cluster_centers_2D = tsne.transform(kmeans.cluster_centers_)

        plt.scatter(vectors_2D[:, 0], vectors_2D[:, 1], c=cluster_labels)
        plt.scatter(cluster_centers_2D[:, 0], cluster_centers_2D[:, 1], c='red', s=200, alpha=0.5)  # Plot centers
        plt.title(title)
        plt.show()

    def plot_3D(self, title):
        # Convert the vectors to 3D using t-SNE
        tsne = TSNE(n_components=3, random_state=0)
        vectors_3D = tsne.fit_transform(self.vector_database)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(vectors_3D[:, 0], vectors_3D[:, 1], vectors_3D[:, 2])
        plt.title(title)
        plt.show()
