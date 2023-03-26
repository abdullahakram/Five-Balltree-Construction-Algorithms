from sklearn.neighbors import BallTree
from sklearn.utils import resample

# X is the input data matrix, k is the number of nearest neighbors to return
n_samples = 1000  # number of samples to use for constructing the initial tree
sampled_X = resample(X, n_samples=n_samples, random_state=0)
tree = BallTree(sampled_X, leaf_size=30)
dist, ind = tree.query(X, k=k)