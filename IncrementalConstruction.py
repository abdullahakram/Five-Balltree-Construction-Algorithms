from sklearn.neighbors import BallTree

# X is the input data matrix, k is the number of nearest neighbors to return
tree = BallTree(X[:1], leaf_size=30)
for x in X[1:]:
    dist, ind = tree.query(x.reshape(1, -1), k=1)
    tree.insert(x.reshape(1, -1))
dist, ind = tree.query(X, k=k)