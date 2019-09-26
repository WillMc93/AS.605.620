"""
Implements the Strassen Matrix Multiplication algorithm.

@ authour William McElhenney
@ version 1.0 09/25/2019
"""


from matrix_tools import *

"""
Implements Strassen matrix multiplication

@param matrixA: the first matrix to multiply
@param matrixB: the second matrix to multiply
@return the product of matrixA and matrixB
"""
def strassen(matrixA, matrixB):
	# an assumption
	size = len(matrixA)

	# safety checks
	assert(len(matrixA) == len(matrixB))
	assert (is_square(matrixA) and is_square(matrixB))

	# BASE CASE
	if size == 1:
		return multiply(matrixA, matrixB)

	
	# GENERAL CASE
	matrixC = init_matrix(size)

	# Step 1: Partition the matrices
	partsA = partition(matrixA)
	partsB = partition(matrixB)
	partsC = partition(matrixC)

	# Step 2: Get substitution matrices
	subs = get_subs(partsA, partsB)

	# Step 3: Get products of substitution matrices
	prods = get_prods(partsA, partsB, subs)


	# Step 4: Calculate C11 through C22
	# C11
	partsC[0] = add_sub(prods[4], prods[3]) # P5 + P4
	partsC[0] = add_sub(partsC[0], prods[1], True) # (P5 + P4) - P2
	partsC[0] = add_sub(partsC[0], prods[5]) # C11 = (P5 + P4 - P2) + P6

	# C12
	partsC[1] = add_sub(prods[0], prods[1]) # C12 = P1 + P2

	# C21
	partsC[2] = add_sub(prods[2], prods[3]) # C21 = P3 + P4

	# C22
	partsC[3] = add_sub(prods[4], prods[0]) # P5 + P1
	partsC[3] = add_sub(partsC[3], prods[2], True) # (P5 + P1) - P3
	partsC[3] = add_sub(partsC[3], prods[6], True) # C22 = (P5 + P1 - P3) + P7

	return departition(partsC)


"""
Partitions matrix into quarters.
Defined here instead of matrix_tools due to specialization.
IRL I'd probably use numpy to make this whole thing easier.

@param matrix: the matrix to partition
@return list of the partitions

"""
def partition(matrix):
	assert(is_square(matrix))

	size = int(len(matrix) / 2) # but why, Python?

	partitions = []
	for i in range(4):
		partitions.append(init_matrix(size))

	for i in range(size):
		for j in range(size):
			partitions[0][i][j] = matrix[i][j] # 1,1
			partitions[1][i][j] = matrix[i][j + size] # 1,2
			partitions[2][i][j] = matrix[i + size][j] # 2,1
			partitions[3][i][j] = matrix[i + size][j + size] # 2,2

	return partitions

"""
Returns a matrix consisting of the quarter partions.

@param parts: the partitions that we want to put back together
@return the matrix of the combined parts
"""
def departition(parts):
	# IRL we should probably put a safety check here
	# to make sure the size of the parts is equal

	size = len(parts[0])
	matrix = init_matrix(2*size)

	for i in range(size):
		for j in range(size):
			matrix[i][j] = parts[0][i][j]
			matrix[i][j + size] = parts[1][i][j]
			matrix[i + size][j] = parts[2][i][j]
			matrix[i + size][j + size] = parts[3][i][j]

	return matrix


"""
Creates substitution matrices S1 through S10 from the partitions pA and pB.
The book calls the submatrices, but I think substituition is more fitting.

@param pA: partitions of matrixA
@param pB: partitions of matrixB
@return subs: list contains the substitution matrices S1 - S10
"""
def get_subs(pA, pB):

	subs = []

	# NOTE: indexes 0 = 1,1; 1 = 1,2; 2=2,1; 3=2,2
	# Sorry about the block of black box code.
	subs.append(add_sub(pB[1], pB[3], True)) # S1 = B12 - B22
	subs.append(add_sub(pA[0], pA[1])) # S2 = A11 + A12
	subs.append(add_sub(pA[2], pA[3])) # S3 = A21 + A22
	subs.append(add_sub(pB[2], pB[0], True)) # S4 = B21 - B11
	subs.append(add_sub(pA[0], pA[3])) # S5 = A11 + A22
	subs.append(add_sub(pB[0], pB[3])) # S6 = B11 + B22
	subs.append(add_sub(pA[1], pA[3], True)) # S7 = A11 - A22
	subs.append(add_sub(pB[2], pB[3])) # S8 = B21 + B22
	subs.append(add_sub(pA[0], pA[2], True)) # S9 = A11 - A21
	subs.append(add_sub(pB[0], pB[1])) # S10 = B11 + B12

	return subs

"""
Creates the matrix products P1 through P7

@param pA: partitions of matrixA
@param pB: partitions of matrixB
@param subs: list containing the substitution matrices
@return prods: the specified products for Strassen
"""
def get_prods(pA, pB, subs):

	prods = []

	prods.append(strassen(pA[0], subs[0])) # P1 = A11 * S1
	prods.append(strassen(subs[1], pB[3])) # P2 = S2 * B22
	prods.append(strassen(subs[2], pB[0])) # P3 = S3 * B11
	prods.append(strassen(pA[3], subs[3])) # P4 = A22 * S4
	prods.append(strassen(subs[4], subs[5])) # P5 = S5 * S6
	prods.append(strassen(subs[6], subs[7])) # P6 = S7 * S8
	prods.append(strassen(subs[8], subs[9])) # P7 = S9 * S10

	return prods