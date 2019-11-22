from itertools import product
import sys

sys.path.append('./code/')

import LCS
import fileIO

if __name__ == '__main__':
	# error check input arguments
	if len(sys.argv) >  2:
		print("Too few arguments; need an input path and an output path")
		quit()
	elif len(sys.argv) < 4:
		print("Too many arguments; just need an input path and an output path")
		quit()

	input_path = sys.argv[1]
	output_path = sys.argv[2]

	sequences = fileIO.read_input(input_path)

	# find the LCS
	for seq1, seq2 in product(sequences):
		lcs = LCS(seq1, seq2)

		fileIO.write_output(lcs.LCS)