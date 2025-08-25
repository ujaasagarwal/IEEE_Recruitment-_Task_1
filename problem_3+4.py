import numpy as np
import random

matrix=np.random.randint(1 , 101 , size = (5,5))

print(f"original matrix is {matrix}")

max = matrix.max()
min = matrix.min()
mean=matrix.mean()

print(f"Maximum value is {max}\nMinimum value is {min}\nMean Value is {mean}")

normalized = (matrix - min)/(max-min)

print(f"normalized array is {np.round(normalized , 2)}")


sorted_flatten=np.sort(matrix.flatten())

print(f"the sorted flattened array is {sorted_flatten}")

new_matrix=matrix[1:4 , 1:4]
print(f"the centre matrix is {new_matrix}")

firstrow=new_matrix[0 , :]
firstcolumn=new_matrix[: ,0]

print(f"first row is {firstrow}\nfirst column is {firstcolumn}")

print(f"the dot product of the two is {np.dot(firstrow , firstcolumn)}")