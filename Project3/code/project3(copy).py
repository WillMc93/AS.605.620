"""
Project 3 - Longest-Common Subsequence

Here's the main script for the program which accepts the input arguments and
ensures everything completes.

@authour Will McElhenney
@date 12/1/2019
"""

# library imports
import sys
from itertools import product

# append code to the pypath
sys.path.append('./code/')

# import our custom code
import LCS
import fileIO

"""
MAIN

Checks the input arguments and runs the program. 
"""
if __name__ == '__main__':
	# error check input arguments
	if len(sys.argv) < 3:
		print("Too few arguments; need an input path and an output path.")
		quit()
	elif len(sys.argv) > 3:
		print("Too many arguments; only need an input path and an output path.")
		quit()

	in_path = sys.argv[1]
	out_path = sys.argv[2]

	# check that input file exists
	try:
		temp = open(in_path, 'r')
	except IOError:
		print(f"Input path {in_path} could not be found.")
		quit()

	# initialize the output file
	try:
		fileIO.init_outp(in_path, out_path)
	except IOError:
		print(f"Output path {out_path} could not be reached. Please make sure "
				"that the directory exists.")
		quit()

	# file iterators for loop
	gen1 = fileIO.gen_sequences(in_path)
	gen2 = fileIO.gen_sequences(in_path)

	# loop through sequence combinations
	for (lbl1, seq1), (lbl2, seq2) in product(gen1, gen2):
		# ignore same sequence
		if lbl1 == lbl2:
			continue

		# build the LCS matrix
		b_matrix, c_matrix = LCS.calc_lcs(seq1, seq2)

		# rebuild the LCS
		lcs_seq = LCS.build_seq(b_matrix, seq1, seq2)

		# command-line report
		print(f"LCS of {lbl1} and {lbl2} is {lcs_seq}.")

		# write LCS to output
		fileIO.write_outp(lbl1, lbl2, lcs_seq, out_path)
	
	# keeps output cleaner
	print("\n")


