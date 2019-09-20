"""
605.420 Project 1 - Matrix Multiplication

William McElhenney
9/24/19	
"""

"""
Generator function that reads in the data and
converts in to a usable form (size, matrix A, matrix B)
"""
def read(path='\\inputs\\classdata.dat')
	# get that data
	data = None
	with open(path) as file:
		# just read the whole thing in and split at the newlines
		data = file.read()
		data = data.split('\n')

		# cleanup data (strip whitespace from termini)
		for line in data:
			line = line.strip()

	# das generator loop
	done = False

	while not done:
		# storage
		size = 0
		matrixA = []
		matrixB = []

		# Break the data into proper chunks.
		size = data[0]
		matrices = data[1: 2*size + 1]

		matrixA = matrices[0: size]
		matrixB = matrices[size: 2*size]

		# break up the matrix data into matrices
		for line in matrixA:
			line = line.split(' ')
			if len(line) != size:
				raise IndexError("The data for matrixA is improperly formatted.")
		for line in matrixB:
			line = line.split(' ')
			if len(line) != size:
				raise IndexError("The data for matrixB is improperly formatted.")

		# remove isolated data
		# It's a bold strategy, Cotton. Let's see if it pays off for him.
		if len(data) > 2*size + 1:
			data = data[2*size + 2:]
		else:
			done = True

		# yield the matrices
		yield size, matrixA, matrixB

	yield None, None, None

"""
Makes a em-by-en matrix of all zeros.
"""
def init_matrix(m, n):
	return [[0] * n for _ in range(m)]

"""
Implements basic matrix multiplication, O(n^3)
"""
def basic(size, matrixA, matrixB):
	# initialize output matrix
	outp = init_matrix(size, size)

	# iterate through rows of matrixA
	for m in range(size):
   		# iterate through columns of matrixB
   		for n in range(size):
       		# iterate through rows of matrixB
       		for n2 in range(size):
           		result[m][n] += matrixA[m][n2] * matrixB[n2][n]

    return outp

"""
Outputs the results
"""
def write(matrixA, matrixB, basic_time, s_time, path='\\outputs\\test.out'):
	with open(path, 'a+'):
