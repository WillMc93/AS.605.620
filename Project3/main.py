import sys
from itertools import product

sys.path.append('./code/')

import LCS
import fileIO


if __name__ == '__main__':
	# error check input arguments
	if len(sys.argv) < 3:
		print("Too few arguments; need an input path and an output path")
		quit()
	elif len(sys.argv) > 3:
		print("Too many arguments; just need an input path and an output path")
		quit()

	input_path = sys.argv[1]
	output_path = sys.argv[2]
	#import pdb
	#pdb.set_trace()

	sequences = fileIO.read_inp(input_path)
	# find the LCS
	for seqA, seqB in product(sequences, sequences):
		if seqA == seqB:
			continue
		
		# get the actual sequence
		seq1 = sequences[seqA]
		seq2 = sequences[seqB]

		lcs = LCS.calc_lcs(seq1, seq2)
		fileIO.write_outp(seq1, seq2, lcs, output_path)