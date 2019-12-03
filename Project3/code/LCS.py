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
def init_matrix(m,n, fill_val=0):
	return [[fill_val] * n for _ in range(m)]

"""
Function for dynamic calculation of the LCS sequence length. 
Generates a matrix where the (0,0) position is the length of the LCS.

@param seq1: the first sequence
@param seq2: the second sequence

@return a filled in 2d LCS matrix
"""
def calc_lcs(seq1, seq2):
	m = len(seq1)
	n = len(seq2)

	b_matrix = init_matrix(m, n, '')
	c_matrix = init_matrix(m+1, n+1)

	# define loop dimension
	rng1 = range(m)
	rng2 = range(n)

	# c and b value holders
	b = None
	c = None

	import pdb
	#pdb.set_trace()

	for i in rng1:
		for j in rng2:
			if seq1[i] == seq2[j]:
				b = 'diag'
				c = c_matrix[i][j] + 1

			else:
				up = c_matrix[i][j+1]
				left = c_matrix[i+1][j]

				c, b = (up, 'up') if up >= left else (left, 'left')

			b_matrix[i][j] = b
			c_matrix[i+1][j+1] = c

	return b_matrix, c_matrix


"""
Function for identifying the exact LCS sequence from the LCS-matrix.

@param b_matrix: the directional matrix (b)
@param seq1: the sequence for the rows of the LCS matrix
@param seq2: the sequence for the cols of the LCS matrix

@return the LCS sequence
"""
def build_seq(b_matrix, seq1, seq2, i=None, j=None):

	lcs_seq = ''

	if i == None or j == None:
		i = len(seq1) - 1
		j = len(seq2) - 1

	while (i >= 0 and j >= 0):
		if b_matrix[i][j] == 'diag':
			lcs_seq = seq1[i] + lcs_seq 
			i -= 1
			j -= 1
		elif b_matrix[i][j] == 'up':
			i -= 1
		elif b_matrix[i][j] == 'left':
			j -= 1

		else:
			# uh oh
			raise IOError

	return lcs_seq
