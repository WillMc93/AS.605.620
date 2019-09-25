import re

"""
Makes a embien matrix of all zeros.
"""
def init_matrix(m, n=None):
	if n is None:
		n = m

	return [[0] * n for _ in range(m)]

"""
Converts matrix strings into lists of values.
"""
def make_matrix(matrix):
	for idx in range(len(matrix)):
		line = matrix[idx]
		line = re.split(r'\s+', line)

		for jdx in range(len(line)):
			line[jdx] = int(line[jdx])


		matrix[idx] = line

	return matrix

"""
Check that the given matrix is square
"""
def is_square(matrix, size):
	if len(matrix) != size:
		raise IndexError

	for row in matrix:
		if len(row) != size:
			raise IndexError

	return True

"""
Implements basic matrix multiplication, O(n^3)
"""
def multiply(matrixA, matrixB):
	# an assumption
	size = len(matrixA)

	# safety checks
	assert(len(matrixA) == len(matrixB))
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

"""
Adds (or subtracts, depending on sub) two matrices.
Didn't want two functions with 99.9% the same code
"""
def add_sub(matrixA, matrixB, sub=False):
	# an assumption
	size = len(matrixA)

	# some safety checks
	assert(len(matrixA) == len(matrixB))
	assert(is_square(matrixA, size) and is_square(matrixB, size))
	

	# do it
	outp = init_matrix(size)

	mod = 1 if sub == False else -1

	for i in range(size):
		for j in range(size):
			outp[i][j] = matrixA[i][j] + mod * matrixB[i][j]

	return outp