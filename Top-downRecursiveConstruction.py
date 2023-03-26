from sklearn.neighbors import BallTree

# X is the input data matrix, k is the number of nearest neighbors to return
tree = BallTree(X, leaf_size=30)
dist, ind = tree.query(X, k=k)
