"""
605.420 Project 1 - Matrix Multiplication

William McElhenney
9/24/19	
"""


import sys

sys.path.append('./code/')

# custom code
from fileIO import read, write
from matrix_tools import multiply
from strassen import strassen

# MAIN
if __name__ == '__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]

	# Reinitialize output file if it already exists
	with open(outfile, 'w+') as file:
		file.write('')

	for size, matrixA, matrixB in read(infile):
		productB = multiply(matrixA, matrixB)
		productS = strassen(matrixA, matrixB)

		assert(productB == productS)

		write(matrixA, matrixB, productB, productS, {'basic': 0, 'strassen': 0}, outfile)
