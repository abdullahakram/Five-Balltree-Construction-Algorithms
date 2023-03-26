from sklearn.neighbors import BallTree
from scipy.spatial.distance import pdist, squareform

# X is the input data matrix, k is the number of nearest neighbors to return
distances = squareform(pdist(X))
tree = BallTree(X, metric='precomputed')
dist, ind = tree.query(X, k=k)