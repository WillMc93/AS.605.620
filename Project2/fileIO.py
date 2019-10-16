"""
William McElhenney


"""

import re

def read(path):

	with open(path) as file:
		
		for data in file:
			if re.fullmatch(r'^[0-9]+\s*\n$', data):
				outp = re.sub(r'\s', '', data)

				yield int(outp)
	return