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

	with open(path) as file:
		# yield data per line
		for data in file:
			# make sure the line is an integer
			if re.fullmatch(r'^[0-9]+\s*\n$', data):
				# get rid of whitespace (what does superfulous mean?)
				outp = re.sub(r'\s', '', data)
				# yeet
				yield int(outp)
	return

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
		file.write("Statistics -- \n")
		file.write(f"\tCollisions: {table.prim_coll_count} \n")

		if len(table.unplaced) < 1:
			file.write("\tAll values were able to be placed into the table. \n")
		else:
			file.write(f"\tUnplaced values: {table.unplaced} \n")

		file.write(f"\tFill Ratio: {table.fill_ratio()} \n")
		