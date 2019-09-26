"""
Module containing the tools needed for matrix manipulation,
including basic matrix multiplication.

@author William McElhenney
@version 1.0 9/25/2019
"""
from re import split # better string spliting funcition

"""
Makes a embien (read M by N) matrix of all zeros.

@param m: the number of columns
@param n: the number of rows
"""
def init_matrix(m, n=None):
	# if n is unspecified make the matrix square
	if n is None:
		n = m

	return [[0] * n for _ in range(m)]

"""
Converts matrix strings into lists of values.

@param matrix: the list containing the raw matrix data (list of strings)
"""
def make_matrix(matrix):
	for idx in range(len(matrix)):
		line = matrix[idx]
		line = split(r'\s+', line)

		for jdx in range(len(line)):
			line[jdx] = int(line[jdx])


		matrix[idx] = line

	return matrix

"""
Check that the given matrix is square.

@param matrix: the matrix to check
@param size: 
"""
def is_square(matrix):
	size = len(matrix)

	# check all rows
	for row in matrix:
		if len(row) != size:
			raise IndexError

	return True

"""
Implements basic matrix multiplication, O(n^3).

@param matrixA: the first matrix to multiply
@param matrixB: the second matrix to mutliply
@return outp: the product of the matrices
"""
def multiply(matrixA, matrixB):
	# an assumption
	size = len(matrixA)

	# safety checks
	assert(len(matrixA) == len(matrixB))
	assert (is_square(matrixA) and is_square(matrixB))

	# initialize output matrix
	outp = init_matrix(size)

	# iterate through rows of matrixA
	for i in range(size):
		# iterate through columns of matrixB
		for j in range(size):
			# iterate through the columns of A and the rows of B
			for k in range(size):
				outp[i][j] += matrixA[i][k] * matrixB[k][j]

	return outp

"""
Adds (or subtracts, depending on sub) two matrices.
Didn't want two functions with 99.9% the same code

@param matrixA: the first matrix to add/sub
@param matrixB: the second matrix to add/sub
@param sub: True if we want to subtract B from A
@return the sum/difference of the matrices
"""
def add_sub(matrixA, matrixB, sub=False):
	# an assumption
	size = len(matrixA)

	# some safety checks
	assert(len(matrixA) == len(matrixB))
	assert(is_square(matrixA) and is_square(matrixB))
	

	# do it
	outp = init_matrix(size)

	mod = 1 if sub == False else -1

	for i in range(size):
		for j in range(size):
			outp[i][j] = matrixA[i][j] + mod * matrixB[i][j]

	return outp