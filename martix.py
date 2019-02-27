import numpy as np

# test
a = np.array([[0.92, 0.39], [0.39, -0.92]])
b = np.array([[3.12, 1.3], [1.3, 0.58]])
c = np.array([[0.92, 0.39], [0.39, -0.92]])
d = np.array([[1, 0.427], [-2.377, 1]])
e = np.transpose(d)
print(np.dot(e, d))
