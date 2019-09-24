from itertools import product as itProduct
from matrix_tools import *

"""
Implements Strassen matrix multiplication
"""

def strassen(size, matrixA, matrixB):
	# check that matrixA and B are square
	assert (is_square(matrixA, size) and is_square(matrixB, size))

	# initialize output matrix
	outp = init_matrix(size)


def partition(matrix):
	size = len(matrix) / 2

	coords = [_ for _ in itProduct([0,1], repeat=2)]

	# initialize the output matrices
	partitions = {}

	for coord in coords:
		partitions[coord] = init_matrix(size)




