import numpy as np
def sumColumn(matrix):
    return np.sum(matrix, axis=1)

matrix1 = np.loadtxt('matrix1.txt').astype(int)
matrix2 = np.loadtxt('matrix2.txt').astype(int)


result = [[matrix1[i][j] + matrix2[i][j]  for j in range
(len(matrix1[0]))] for i in range(len(matrix1))]
  
for r in result:
    print(r)