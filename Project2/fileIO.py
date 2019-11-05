"""
William McElhenney


"""

import re
import hashing

def read_input(path):

	with open(path) as file:
		
		for data in file:
			if re.fullmatch(r'^[0-9]+\s*\n$', data):
				outp = re.sub(r'\s', '', data)

				yield int(outp)
	return

def write_outp(table, path):

	with open(path, 'w') as file:
		file.write(table.to_string())

		file.write("-" * 78 + "\n")

		file.write("Statistics -- \n")
		file.write(f"\tCollisions: {table.prim_coll_count} \n")

		if len(table.unplaced) == 0:
			file.write("\tAll values were able to be placed into the table.")
		else:
			file.write(f"\tUnplaced values: {table.unplaced} \n")
		