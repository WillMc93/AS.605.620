from itertools import product

class LCS:
	def __init__(self, seq1, seq2):
		# idiot check (should be prevented by fileIO)
		assert(len(seq1) > 0 and len(seq2) > 0)

		# initialize the comparison matrix
		_fill = [0 for _ in range(len(seq2) + 1)] # get the vertical lists
		self.matrix = [_fill for _ in range(len(seq1) + 1)] # arrange vertical lists

		self.seq1 = seq1
		self.seq2 = seq2

		LCS()
		self.LCS = build_seq()


	def LCS(self):
		# get loop dimensions
		rng_1 = range(len(self.seq1), -1, -1)
		rng_2 = range(len(self.seq2), -1, -1)
		dims = (rng_1, rng_2)

		# fill matrix (this is just an abstracted nested loop)
		for i,j in product(*dims):
			# if sequences match: 1 + diag value
			if self.seq1[i] == self.seq2[j]:
				self.matrix[i][j] = 1 + matrix[i+1][j+1]
			else:
				tmp_a = self.matrix[i+1][j]
				tmp_b = self.matrix[i][j+1]

				# pick bottom value if >= right-value; else down-value
				self.matrix[i][j] = tmp_a if tmp_a >= tmp_b else tmp_b

	def build_seq(self):
		sequence = ''

		# let m be length of sequence 1
		# and n be length of sequence 2
		m = len(self.seq1)
		n = len(self.seq2)

		i,j = 0,0
		while(i < m and j < n):
			if self.seq1[i] == self.seq2[j]:
				sequence += self.seq1[i]
				i += 1
				j += 1

			elif self.matrix[i+1][j] >= self.matrix[i][j+1]:
				i += 1
			else:
				j += 1

		return sequence
