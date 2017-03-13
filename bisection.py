import numpy as np
from scipy.sparse import coo_matrix

nodes = {0:4, 1:7, 2:8, 3:10, 4:11, 5:12, 6:17, 7:18, 8:19, 9:20,
		 10:21, 11:22, 12:23, 13:24}

data = np.array([1]*34)
row = np.array([0]*2+[1]*2+[2]*3+[3]*1+[4]*3+[5]*2+[6]*3+[7]*3+[8]*3+[9]*2 +
			   [10]*2+[11]*3+[12]*3+[13]*2)
col = np.array([2, 6, 2, 4, 0, 1, 5, 4, 1, 3, 5, 2, 4, 0, 7, 10, 6, 8, 11,
				7, 9, 12, 8, 13, 6, 11, 7, 10, 12, 8, 11, 13, 9, 12])
A = coo_matrix((data, (row, col))).toarray()
B = coo_matrix((data, (row, row))).toarray()
C = np.subtract(B, A)
print(A, B, C, sep='\n\n')

eigenvalues, eigenvectors = np.linalg.eigh(C)
second_eigenvector = eigenvectors[:,1]
print('\n' + 'eigenvector =')
print(second_eigenvector)
average = np.average(second_eigenvector)
print("average =", average)

first_graph = []
second_graph = []

for index, eigvalue in enumerate(second_eigenvector):
	if eigvalue < average:
		first_graph.append(nodes.get(index))
	else:
		second_graph.append(nodes.get(index))

print('first graph:', first_graph)
print('second graph:', second_graph)
input()
