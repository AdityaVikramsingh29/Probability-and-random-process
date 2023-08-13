import numpy as np

A = np.array([1,-1])
B = np.array([-4,6])
C = np.array([-3,-5])

matrix = np.array([[1, 1, 1], [1, -4, -3], [-1, 6, -5]])
rank = np.linalg.matrix_rank(matrix)

print("Since the rank of the matrix is :", rank)
print("Therefore the given points are non collinear.")

