from matrix_tools import is_square, init_matrix

"""
Implements basic matrix multiplication, O(n^3)
"""
def basic(size, matrixA, matrixB):
	# check that matrixA and B are square
	assert (is_square(matrixA, size) and is_square(matrixB, size))

	# initialize output matrix
	outp = init_matrix(size, size)

	# iterate through rows of matrixA
	for m in range(size):
		# iterate through columns of matrixB
		for n in range(size):
			# iterate through rows of matrixB
			for n2 in range(size):
				outp[m][n] += int(matrixA[m][n2]) * int(matrixB[n2][n])

	return outp