"""
605.420 Project 1 - Matrix Multiplication

@ author William McElhenney
@ version 1.0 09/24/19	
"""
import sys

# custom code
sys.path.append('./code/')
from fileIO import read, write
from matrix_tools import multiply
from strassen import strassen

"""
MAIN

Reads in the data, runs the multiplications, 
and gets the results written
"""
if __name__ == '__main__':
	# Get the command line argumentsd
	infile = sys.argv[1]
	outfile = sys.argv[2]

	# Reinitialize output file if it already exists
	with open(outfile, 'w+') as file:
		file.write('')

	# Do the things
	for size, matrixA, matrixB in read(infile):
		productB = multiply(matrixA, matrixB)
		productS = strassen(matrixA, matrixB)

		assert(productB == productS)

		write(matrixA, matrixB, productB, productS, \
			{'basic': 0, 'strassen': 0}, outfile)
