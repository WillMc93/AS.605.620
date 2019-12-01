"""
Functions to deal with file input and output

@authour William McElhenney
@date 11/6/2019
"""

# Imports
import re # regular expressions

"""
Generator function for yielding ints from the input file, path

@param path: string representation of the file path of the input
"""
def gen_sequences(path):

	index = dict()

	label = None
	sequence = None
	
	seq_pattern = re.compile(r'^(?P<name>\S+)\s*=\s*(?P<seq>\S+)\s*$')
	comment_pattern = re.compile(r'^#.*\s*$')
	
	with open(path) as file:
		for line in file:

			# ignore commented lines
			if re.fullmatch(comment_pattern, line):
				continue
			
			match = re.fullmatch(seq_pattern, line)
			
			# if the sequence is valid
			if match:
				# parse the sequence
				label = match.group('name')
				sequence = match.group('seq')

				# change the label as necessary
				if label in index:
					index[label] += 1
					label = f"{label}_{index[label]}"

				# append the label index
				else:
					index[label] = 0
				
			# prevent yielding None, None
			else:
				continue

			# yield the label, seq tuple
			yield label, sequence

	return None

"""
Function for writing the table to the output file, path.
Calls the table's to_string() and pulls the statistics.

@param seq1_name: label of the first sequence
@param seq2_name: label of the second sequence
@param lcs_seq: longest common sequence identified
@param path: string representation of the output file path of the
"""
def write_outp(seq1_name, seq2_name, lcs_seq, path):

	with open(path, 'a') as file:
		file.write(f"LCS of {seq1_name} and {seq2_name}:\n")
		file.write(f"\t{lcs_seq}: Length {len(lcs_seq)}\n")

"""
Function for initializing the output file. Erases already existiing data and
mirrors the input set's labels in the output file.

@param in_path: input file path
@param out_path: output file path.
"""
def init_outp(in_path, out_path):

	with open(out_path, 'w') as file:
		# Report the input in the outputs
		file.write("Read in the sequences labeled: \n")
		for label, _ in gen_sequences(in_path):
			file.write(f"\t{label}\n")

		# Insert Divider
		file.write("=" * 78 + "\n")
