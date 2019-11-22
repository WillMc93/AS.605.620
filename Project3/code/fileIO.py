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
def read_inp(path):

	sequences = dict()
	counter = 0
	
	seq_pattern = re.compile(r'^(?P<name>\S+)\s*=\s*(?P<seq>\S+)$')
	
	with open(path) as file:
		for line in file:
			
			match = re.fullmatch(seq_pattern, line)
			
			# if the sequence is valid and the name is not already in sequences
			if match and match.group('name') not in sequences.keys():
				# add it as is
				sequences[match.group('name')] = match.group('seq')

			# else if the match name is already in sequences
			elif match and match.group('name') in sequences.keys():
				# append the counter 
				sequences[match.group('name') + '_counter'] = match.group('seq')
				counter += 1

	return sequences

"""
Function for writing the table to the output file, path.
Calls the table's to_string() and pulls the statistics.

@param table: hash_table that needs to be written. 
@param path: string representationof the file path of the output
"""
def write_outp(seq1_name, seq2_name, lcs, path):

	with open(path, 'wa') as file:
		file.write(f"LCS of {seq1_name} and {seq2_name}:")
		file.write(f"\t{lcs}")

		