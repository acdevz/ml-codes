from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data # 4 features: sepal length, sepal width, petal length, petal width
y = iris.target # 3 classes: setosa, versicolor, virginica

kmean = KMeans(n_clusters=3, max_iter=10, n_init="auto").fit(x)
labels = kmean.labels_
centroids = kmean.cluster_centers_

ax = plt.figure(figsize=(6, 5)).add_subplot(111, projection='3d')
ax.scatter(x[:, 3], x[:, 0], x[:, 2], c=labels.astype(float), s=50, alpha=0.5, edgecolor='k')
ax.scatter(centroids[:, 3], centroids[:, 0], centroids[:, 2], c='red', s=200, alpha=0.5)

ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
plt.show()