import re

"""
Makes a embien matrix of all zeros.
"""
def init_matrix(m, n):
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
