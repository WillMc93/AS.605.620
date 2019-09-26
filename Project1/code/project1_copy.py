#!/usr/bin/python3
#!/usr/bin/env python3

"""
605.420 Project 1 - Matrix Multiplication

@ author William McElhenney
@ version 1.0 09/24/19	
"""
import sys

# custom code
sys.path.append('./code/') # make sure we can find the following from root
from fileIO import read, write
from matrix_tools import multiply
from strassen import strassen, reset

"""
MAIN

Reads in the data, runs the multiplications, 
and gets the results written
"""
if __name__ == '__main__':
	# Get the command line arguments
	infile = sys.argv[1]
	outfile = sys.argv[2]

	# Reinitialize output file if it already exists
	with open(outfile, 'w+') as file:
		file.write('')

	# Do the things
	try:
		for size, matrixA, matrixB in read(infile):
			productB = multiply(matrixA, matrixB)
			print("Successfully multiplied!")

			reset()
			productS = strassen(matrixA, matrixB)
			print(f"Successfully (Strassen) multiplied! {strassen.counter}")

			assert(productB == productS) # sanity check

			write(matrixA, matrixB, productB, productS, outfile)

	# Need to tell the user so they know to check the file		
	except FileNotFoundError as e:
		print(str(e))

	# Let the user know an error was encountered (should be on their end)
	except Exception as e: 
		print("Something went wrong. The input data is likely has a " + \
			"formatting issue.")
		print("Make sure the input only consists of " + \
			"numbers, and that the size matches the matrix.")
		print('Caught Exception:\n\t\t' + str(e) + "\n\n")
		with open(outfile, 'a+') as file:
			file.write(str(e))
