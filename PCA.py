from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

pca = PCA(n_components=3)  # Reduce to 2 dimensions
iris = load_iris()
x = iris.data  # 4 features: sepal length, sepal width, petal length, petal width
y = iris.target  # 3 classes: setosa, versicolor, virginica

print(x)
PCs = pca.fit_transform(x)  # Fit PCA on the data
print(PCs)  # Output: (150, 2), 150 samples, 2 principal components