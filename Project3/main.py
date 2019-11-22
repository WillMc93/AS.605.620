import sys

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

	sequences = fileIO.read_inp(input_path)

	# find the LCS
	for seq1_key in sequences.keys():
		for seq2_key in sequences.keys():
			if seq1_key == seq2_key:
				continue
			
			seq1 = sequences[seq1_key]
			seq2 = sequences[seq2_key]

			lcs = LCS(seq1, seq2)
			fileIO.write_outp(seq1_key, seq2_key, lcs.LCS, output_path)