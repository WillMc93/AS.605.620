import re # regular expressions for formatting the read-in data

# custom code
from matrix_tools import *

"""
Generator function that reads in the data and
converts in to a usable form (size, matrix A, matrix B)
"""
def read(path):
	# get that data
	data = None
	with open(path) as file:
		# just read the whole thing in and split at the newlines
		data = file.read()
		data = data.split('\n')

	# then cleanup the data
	for idx in range(len(data)):
		line = data[idx]
		line = re.sub('\s+', ' ', line)
		line = line.strip()
		
		data[idx] = line

	# das generator loop
	done = False

	while not done:
		# Initialize storage
		size = 0
		matrixA = []
		matrixB = []

		# Break the data into proper chunks.
		size = int(data[0])

		matrices = data[1: 2*size + 1]
		matrixA = matrices[0: size]
		matrixB = matrices[size: 2*size]
		

		# Take the raw data and turn it into lists of ints.
		matrixA = make_matrix(matrixA)
		matrixB = make_matrix(matrixB)

		# Make sure that the matrices are square
		try:
			is_square(matrixA, size)
		except IndexError:
			print(f"MatrixA: {matrixA}")
			print("The data for matrixA is improperly formatted!")
			return
		try:
			is_square(matrixB, size)
		except IndexError:
			print(f"MatrixB: {matrixB}")
			print("The data for matrixB is improperly formatted!")
			return

		# Remove isolated data
		if len(data) > 2*size + 1:
			data = data[2*size + 2:]
		else:
			done = True

		# Yield the current matrices
		yield size, matrixA, matrixB

	return

"""
Helper function for writing matrices to output file
"""
def write_matrix(matrix, file, delimit='\n'):
	for row in matrix:
		for col in row:
			file.write(str(col) + ' ')

		file.write(delimit)
	file.write('\n')

"""
Outputs the results
"""
def write(matrixA, matrixB, productB, productS, times, path):
	with open(path, 'a+') as file:
		file.write("Inputs:\n")

		write_matrix(matrixA, file)
		write_matrix(matrixB, file)

		file.write("Outputs:\n")
	
		file.write("\tBasic: \n\t\t")
		write_matrix(productB, file, delimit='\n\t\t')

		file.write("\tStrassen: \n\t\t")
		write_matrix(productS, file, delimit='\n\t\t')

		file.write("\nSTATS:")
		file.write(f"\n\tAverage completion time for basic multiplication: {times['basic']}")
		file.write(f"\n\tAverage completion time for strassen multiplication: {times['strassen']}")

		file.write(f"\n{'-' * 78}\n\n")