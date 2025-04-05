import pandas
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

customer_data = pandas.read_csv('./Data/Mall_Customers.csv').iloc[:, 2:5]
print(customer_data.head())

dendrogram = sch.dendrogram(sch.linkage(customer_data, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.axhline(y=300, color='r', linestyle='--')
plt.show()

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=4, linkage='ward')
cluster.fit_predict(customer_data)

plt.figure(figsize=(8, 5))
plt.scatter(customer_data["Annual Income (k$)"], customer_data["Spending Score (1-100)"], c=cluster.labels_, cmap='rainbow')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()