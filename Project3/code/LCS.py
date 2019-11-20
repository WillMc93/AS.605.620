from itertools import product

def LCS(seq1, seq2, expected=None):

	# idiot check (should be prevented by fileIO)
	assert(len(seq1) > 0 and len(seq2) > 0)

	# initialize the comparison matrix
	_fill = [(0, '') for _ in range(len(seq2) + 1)] # get the vertical lists
	matrix = [_fill for _ in range(len(seq1) + 1)] # arrange vertical lists

	"""
	# initialize the solution matrix
	_fill = ['' for _ in range(len(seq2) + 1)]
	solution = [_fill for _ in range(len(seq1) + 1)]
	"""

	max_len = 0

	# tuple of comp_matrix dimensions
	dims = (range(1, len(seq1) + 1), range(1, len(seq2) + 1))

	# nested loop but cleaner
	for i,j in product(*dims):
		if (seq1[i-1] == seq2[j-1]):
			matrix[i][j] = (matrix[i-1][j-1] + 1, 'diag')
			

		else:
			temp_a = matrix[i-1][j]
			temp_b = matrix[i][j-1]

			matrix[i][j] = (temp_a, 'up') if temp_a >= temp_b else (temp_b, 'left')

			matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])






