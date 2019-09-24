"""
605.420 Project 1 - Matrix Multiplication

William McElhenney
9/24/19	
"""

"""
Generator function that reads in the data and
converts in to a usable form (size, matrix A, matrix B)
"""
def read(path='C:\\Users\\whm0004\\Google Drive\\Algorithms\\git\\Project1\\inputs\classinput.dat'):
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
		size = int(data[0])
		matrices = data[1: 2*size + 1]

		matrixA = matrices[0: size]
		matrixB = matrices[size: 2*size]

		# break up the matrix data into matrices
		matrixA = make_matrix(matrixA)
		matrixB = make_matrix(matrixB)
		
		# make sure that the matrices are mostly square
		# (we'll probably check again, but here's a good spot too)
		if len(matrixA) != len(matrixA[0]) != size:
			raise IndexError("The data for matrixA is improperly formatted!")
		if len(matrixB) != len(matrixB[0]) != size:
			raise IndexError("The data for matrixB is improperly formatted!")


		print(matrixA, matrixB)

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
Converts matrix strings into lists of values.
"""
def make_matrix(matrix):
	for idx in range(len(matrix)):
		line = matrix[idx]
		line = line.strip()
		line = line.split(' ')

		matrix[idx] = line

	return matrix

"""
Implements basic matrix multiplication, O(n^3)
"""
def basic(size, matrixA, matrixB):
	# check that matrixA and B are (mostly) square
	assert (len(matrixA) == len(matrixA[0]) == size)
	assert (len(matrixB) == len(matrixB[0]) == size)

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
Function for writing matrices to output (file)
"""
def write_matrix(matrix, file):
	for row in matrix:
		for col in row:
			file.write(num + ' ')

		file.write('\n')

"""
Outputs the results
"""
def write(matrixA, matrixB, product, times, path='\\outputs\\test.out'):
	with open(path, 'a+') as file:
		file.write("Inputs:\n")

		write_matrix(matrixA, file)
		write_matrix(matrixB, file)

		file.write("Outputs:\n")

		write_matrix(product, file)

		file.write('\n\n')

		file.write(f"Average completion time for basic multiplication: {times['basic']}")
		file.write(f"Average completion time for strassen multiplication: {times['strassen']}")


if __name__ == '__main__':
	for size, matrixA, matrixB in read():
		product = basic(size, matrixA, matrixB)
		write(matrixA, matrixB, product, {'basic': 0, 'strassen': 0})
