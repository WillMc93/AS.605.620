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
def init_matrix(m,n, fill=0):
	fill = [0] * (n)
	return [fill for _ in range(m)]

"""
Function for dynamic calculation of the LCS sequence length. 
Generates a matrix where the (0,0) position is the length of the LCS.

@param seq1: the first sequence
@param seq2: the second sequence

@return a filled in 2d LCS matrix
"""
def calc_lcs(seq1, seq2):
	# local variable declarations
	dims = (len(seq1), len(seq2))
	c_matrix = init_matrix(dims[0]+1, dims[1]+1) # c
	b_matrix = init_matrix(*dims, fill='') # b
		
	# define loop dimensions
	rng1 = range(dims[0]+1)
	rng2 = range(dims[1]+1)

	# fill matrix (this is just an abstracted nested loop)
	for i,j in product(rng1, rng2):

		# c and b values we fill into respective matrices
		c = None
		b = None

		# skip first row/column
		if i == 0 or j == 0:
			continue
		
		# if the values match at i,j
		if seq1[i-1] == seq2[j-1]
			c = 1 + c_matrix[i-1][j-1]
			b = 'diag'

		# else we need to check the up and left values
		else:
			up = c_matrix[i-1][j]
			left = c_matrix[i][j-1]
			
			# pick the maximum of the adjacent values
			c, b = up, 'up' if up >= left  else left, 'left'

		# debug check
		assert(c is not None and b is not None)

		c_matrix[i][j] = c
		b_matrix[i][j] = b

	return c_matrix, b_matrix

"""
Function for identifying the exact LCS sequence from the LCS-matrix.

@param seq1: the sequence for the rows of the LCS matrix
@param seq2: the sequence for the cols of the LCS matrix
@param b_matrix: the directional matrix (b)

@return the LCS sequence
"""
def build_seq(b_matrix, seq1, seq2, i=None, j=None):

	if i is None or j is None:
		i = len(seq1)
		j = len(seq2l)

	if i == 0 or j == 0:
		return ''

	if b_matrix[i][j] == 'diag':
		return build_seq(b_matrix, seq1, seq2, i-1, j-1) + seq1[i]

	elif b_matrix[i][j] == 'up':
		return build_seq(b_matrix, seq1, seq2, i-1, j)

	else:
		return build_seq(i-1, j, seq1, seq2, matrix)