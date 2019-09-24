"""
605.420 Project 1 - Matrix Multiplication

William McElhenney
9/24/19	
"""


import sys

sys.path.append('./code/')

# custom code
from fileIO import read, write
from basic import basic
from strassen import strassen

# MAIN
if __name__ == '__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]

	# Reinitialize output file if it already exists
	with open(outfile, 'w+') as file:
		file.write('')

	for size, matrixA, matrixB in read(infile):
		productB = basic(size, matrixA, matrixB)
		write(matrixA, matrixB, productB, None, {'basic': 0, 'strassen': 0}, outfile)
