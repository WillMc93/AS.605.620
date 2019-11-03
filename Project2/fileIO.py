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

def write_output(table, path):

	with open(path, 'w') as file:
		file.write(table.to_string())

		file.write("-" * 78)

		file.write("Statistics: \n")
		file.write(f"Collisions: {table.collisions} \n")
		file.write(f"Unplacable: {table.not_placed} \n")


