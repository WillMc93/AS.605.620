"""
Functions to deal with file input and output

@authour William McElhenney
@date 11/6/2019
"""

# Imports
import re # regular expressions
import hashing # need to recoginze hash table object


"""
Generator function for yielding ints from the input file, path

@param path: string representation of the file path of the input
"""
def read_input(path):

	sequences = dict()
	counter = 0
	
	seq_pattern = re.compile(r'^(?P<name>[.]+)\s*=\s*(?P<seq>\S+)$')
	
	with open(path) as file:
		for line in file:
			
			match = re.fullmatch(seq_pattern, line)
			
			# if the sequence is valid and the name is not already in sequences
			if match and match.group('name') not in sequence.keys():
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
def write_outp(table, path):

	with open(path, 'w') as file:
		# write the table entries
		file.write(table.to_string())

		# write a seperator
		file.write("-" * 78 + "\n")

		# write statistics
		file.write("\nStatistics -- \n")
		file.write(f"\tCollisions: {table.prim_coll_count} \n")

		if len(table.unplaced) < 1:
			file.write("\tAll values were able to be placed into the table. \n")
		else:
			file.write(f"\tUnplaced values: {table.unplaced} \n")

		file.write(f"\tFill Ratio: {table.fill_ratio()} \n")
		