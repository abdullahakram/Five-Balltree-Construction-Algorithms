from sklearn.neighbors import BallTree

# X is the input data matrix, k is the number of nearest neighbors to return
n_levels = 5  # number of levels in the tree
tree = BallTree(X, leaf_size=30, copy_data=False)
for i in range(n_levels):
    _, leaf_idxs = tree.query(X, k=2, return_distance=False)
    tree = BallTree(X[leaf_idxs.flatten()], leaf_size=30, copy_data=False)
dist, ind = tree.query(X, k=k)