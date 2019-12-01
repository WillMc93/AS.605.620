"""
Functions to calculate and return the LCS of two given sequences.

@authour Will McElhenney
@date 12/1/2019
"""

from itertools import product

"""
Function to make an empty matrix for lcs calculation.

@param m: length of sequence 1, rows
@param n: length of sequence 2, cols

@ return an initialized m+1 by n+1 2d list
"""
def init_matrix(m,n):
	fill = [0] * (n+1)
	return [fill for _ in range(m+1)]

"""
Function for bottom-up dynamic calculation of the LCS sequence length. 
Generates a matrix where the (0,0) position is the length of the LCS.

@param seq1: the first sequence
@param seq2: the second sequence

@return a filled in 2d LCS matrix
"""
def calc_lcs(seq1, seq2):
	# local variable declarations
	dims = (len(seq1), len(seq2))	
	matrix = init_matrix(*dims)
	
	# get loop dimensions
	rng1 = range(dims[0], -1, -1)
	rng2 = range(dims[1], -1, -1)

	import pdb
	#pdb.set_trace()

	# fill matrix (this is just an abstracted nested loop)
	for i,j in product(rng1, rng2):
		
		# if in one of the last cells
		if i == dims[0] or j == dims[1]:
			continue

		# if sequences match: 1 + diag value
		if seq1[i] == seq2[j]:
			matrix[i][j] = 1 + matrix[i+1][j+1]

		# else we need to check the right and down values
		else:
			right = matrix[i+1][j]
			down = matrix[i][j+1]

			# pick bottom value if >= right-value; else down-value
			matrix[i][j] = right if right >= down else down

	return matrix

"""
Function for identifying the exact LCS sequence from the LCS-matrix.

@param seq1: the sequence for the rows of the LCS matrix
@param seq2: the sequence for the cols of the LCS matrix
@param matrix: the LCS matrix

@return the LCS sequence
"""
def build_seq(seq1, seq2, matrix):
	sequence = ''

	# let m be length of sequence 1
	# and n be length of sequence 2
	m = len(seq1)
	n = len(seq2)

	i,j = 0,0
	while(i < m and j < n):
		if seq1[i] == seq2[j]:
			sequence += seq1[i]
			i += 1
			j += 1

		elif matrix[i+1][j] >= matrix[i][j+1]:
			i += 1

		else:
			j += 1

	return sequence
