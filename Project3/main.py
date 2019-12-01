import sys
from itertools import product

sys.path.append('./code/')

import LCS
import fileIO


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

	# initialize output file
	fileIO.init_outp(in_path, out_path)

	# find the LCS
	gen1 = fileIO.gen_sequences(in_path)
	gen2 = fileIO.gen_sequences(in_path)

	for (lbl1, seq1), (lbl2, seq2) in product(gen1, gen2):
		# ignore same sequence
		if lbl1 == lbl2:
			continue
		
		lcs = LCS.calc_lcs(seq1, seq2)
		lcs_seq = LCS.build_seq(seq1, seq2, lcs)
		fileIO.write_outp(lbl1, lbl2, lcs_seq, out_path)