"""
Functions to manage file input and output

@authour William McElhenney
@date 12/1/2019
"""

# Imports
import re # regular expressions

"""
Generator function for yielding the labels and sequences from the input file.

@param path: string representation of the input file path
"""
def gen_sequences(path):

	# allows us to read data with the same labels
	index = dict()

	# yieldables
	label = None
	sequence = None
	
	# regex patterns
	seq_pattern = re.compile(r'^(?P<name>\S+)\s*=\s*(?P<seq>.+)\s*$')
	comment_pattern = re.compile(r'^#.*\s*$')

	with open(path) as file:
		# parse each line
		for line in file:
			# ignore commented lines
			if re.fullmatch(comment_pattern, line):
				continue
			
			# ignore unclear sequences (those that have two or more equal signs)
			# I couldn't make a regex that worked for this for some reason
			equality_count = 0
			for char in line:
				if char == '=':
					equality_count += 1
					if equality_count > 1:
						break

			if equality_count > 1:
				continue

			# Parse for valid sequences
			match = re.fullmatch(seq_pattern, line)
			
			# if the sequence is valid
			if match:
				# parse the sequence
				label = match.group('name')
				sequence = match.group('seq')

				# check that a full sequence did get read
				# makes sure that there's no 'empty' data of the form 'label = '
				if len(sequence) < 2:
					continue

				# update the label as necessary
				if label in index:
					index[label] += 1
					label = f"{label}_{index[label]}"

				# append the label index
				else:
					index[label] = 0
				
			# prevent yielding None, None
			else:
				print(f"Failed to parse line: {line}")
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
		# report the compared sequences and their LCS and LCS length
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
