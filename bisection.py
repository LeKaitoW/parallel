import numpy as np
from scipy.sparse import coo_matrix

data = np.array([1]*34)
row = np.array([0]*2+[1]*2+[2]*3+[3]*1+[4]*3+[5]*2+[6]*3+[7]*3+[8]*3+[9]*2 +
			   [10]*2+[11]*3+[12]*3+[13]*2)
col = np.array([2, 6, 2, 4, 0, 1, 5, 4, 1, 3, 5, 2, 4, 0, 7, 10, 6, 8, 11,
				7, 9, 12, 8, 13, 6, 11, 7, 10, 12, 8, 11, 13, 9, 12])
A = coo_matrix((data, (row, col))).toarray()
B = coo_matrix((data, (row, row))).toarray()
print(A)
print()
print(B)
print()
C = np.subtract(B, A)
print(C)
print()
eigvalues, eigvectors = np.linalg.eigh(C)
print("eigvector =")
print(eigvectors[1])
average = np.average(eigvectors[1])
print("average = ", average)

first_graph = []
second_graph = []

eigvector = eigvectors[1].tolist()

for index, eigvalue in enumerate(eigvector):
	if eigvalue < average:
		first_graph.append(index)
	else:
		second_graph.append(index)

print(first_graph)
print(second_graph)
input()
