import numpy as np
def sumColumn(matrix):
    return np.sum(matrix, axis=1)

matrix = np.loadtxt('test.txt').astype(int)

x = 1

sum = sumColumn(matrix)

for i in sum:
	print("sum of column {x} = {sum}".format( x = x , sum = i))
	x += 1

x = 1
for i in matrix:
	print("sum of row {x} = {sum}".format(x=x, sum = i.sum(axis=0) ) )
	x += 1