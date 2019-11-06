#!/usr/bin/python3
#!/usr/bin/env python3

"""
605.420.81 Project 2 - Hash Tables

File containing the parts necessary to run this sucker "safely."

@authour William McElhenney
@date 11/6/2019
"""

# Realitive path to the code folder
sys.path.append('./code/')

# Imports
import hashing # our hash table object
import fileIO # our fileIO functions
import sys # parameter grabbing
import re # regular expressions

# Useful lists/dicts
DEFAULTS = {'input': '', 'output': './outputs/default_output.txt', \
						'hash_func': 'class', 'mod': 120, 'bucket_size': 1, \
						'collision': 'quadratic', 'c': [0,1]}

INT_PARAMS = ['mod', 'bucket_size']

# Regex patterns
param_pat = r'^(?P<parameter>[A-Za-z_]+)=(?P<value>.+)$'
c_pat = r'\[(?P<c1>[0-9]+.{0,1}[0-9]*),[\s]*(?P<c2>[0-9]+.{0,1}[0-9]*)\]'
int_pat = r'[0-9]+'
str_pat = r'[A-Za-z0-9/\\._]+'

# parameter initialization
parameters = DEFAULTS.copy()

"""
Function for the help menu because I couldn't remember when I was testing.

Can be invoked by calling 'python3 project2.py --help' from terminal.
"""
def help():
	print("Usage: project2.py [input_path] [output_path] [hash_func] [mod]", \
				"[bucket_size] [collision] [c]")
	print("Arguments may be entered positionally as above, ", \
			"or with prefixes (e.g. --input_path=[path])")
	print("If using a named parameter all must be named ", \
			"(except for input and output which are checked for).")
	print("Defaults: 'class', 120, 1, ", \
			"'quadratic', [0,1]")
	print("\nOptions: ")
	print("\thash_func: choose between 'class' or 'student'")
	print("\tmod: mod value for class hash")
	print("\tbucket_size: size of buckets")
	print("\tcollision: 'linear' 'quadratic' or 'chaining'")
	print("\tc: c1 and c2 for quadratic in list i.e. [c1,c2]")

"""
Function to parse a non-positional argument. Non-positional arguments take the
form [param]=[value] when called from terminal.

@param option: string that should be of the form [parm]=[value] for setting 
				the table arguments
"""
def parse(option):
	# Check option for parameter match
	form = re.fullmatch(param_pat, option)

	# Ooops, not valid
	if not form:
		print(f"Parameter, {option}, is not formatted correctly valid. "
				"This likely results in default behviour.")
		return None

	# Set the parameter
	else:
		param = form.group('parameter')
		value = form.group('value')

		# if the specified param is not valid, let the user know.
		if param not in DEFAULTS.keys():
			print(f"The parameter, {param}, is not a valid option. " \
					"This likely results in default behaviour.")
			return None
		
		# mod or bucket size parameters
		if param in INT_PARAMS:
			int_param = re.fullmatch(int_pat, value)

			if int_param:
				return param, int(value)

			else:
				print(f"The value for parameter, {param}, is not an ", \
					"integer. This results in default behaviour.")

		# string parameters
		elif param != 'c':
			str_param = re.fullmatch(str_pat, value)

			if str_param:
				return param, value

			else:
				print(f"The value for parameter, {param}, in not an ", \
						"valid string. This results in default behaviour.")

		# c parameters
		elif param == 'c':
			c_param = re.fullmatch(c_pat, value)
			if c_param:
				c1 = c_param.group('c1')
				c2 = c_param.group('c2')

				c1 = float(c1)
				c2 = float(c2)

				return param, [c1,c2]

			else:
				print(f"The c parameters, {value}, are not valid. ", \
						"This results in default behaviour ([0,1]).")

		# Shouldn't get down here
		return None

def set_params():
	# if no parameters were provided bring up help menu
	if len(sys.argv) == 1:
		help()
		return

	# if only one parameter was provided and it is for help
	if len(sys.argv) == 2 and sys.argv[1] == '--help':
		help()
		return

	# Check to see if input parameters are positional
	positional = True
	for elem in sys.argv[1:]:
		if '=' in elem:
			positional = False
			break

	# Clean input to lower cases (except paths)
	for i in range(len(sys.argv[3:])):
		sys.argv[i] = sys.argv[i].lower()

	# If they are positional set our options
	if positional:
		parameters['input'] = sys.argv[1]
		
		if len(sys.argv) > 2:
			parameters['output'] = sys.argv[2]
		if len(sys.argv) > 3:
			parameters['hash_func'] = sys.argv[3]
		if len(sys.argv) > 4:
			parameters['mod'] = int(sys.argv[4])
		if len(sys.argv) > 5:
			parameters['bucket_size'] = int(sys.argv[5])
		if len(sys.argv) > 6:
			parameters['collision'] = sys.argv[6]
		if len(sys.argv) > 7:
			c = re.fullmatch(c_pat, sys.argv[7])

			if c:
				c1 = c.group('c1')
				c2 = c.group('c2')

				c1 = float(c1)
				c2 = float(c2)

				parameters['c'] = [c1,c2]
		return
		
	else: 
		# Set the named parameters.
		for elem in sys.argv[1:]:
			# Parse the input
			option = parse(elem)

			# Set the param
			if option:
				parameters[option[0]] = option[1]

			else:
				# If the option didn't match the user has been notified, and we 
				# just default.
				continue

		# check that input has been set
		if parameters['input'] == '':
			print("No input path was provided. Check your input and try again.")
			raise ValueError

	return

"""
MAIN function
"""
if __name__ == '__main__':
	# Run the set parameters function. Takes care of all input parameters.
	try:
		set_params()
	except ValueError:
		quit()

	# Unpack parameters
	input_path = parameters['input']
	output_path = parameters['output']
	hash_func = parameters['hash_func']
	mod = parameters['mod']
	bucket_size = parameters['bucket_size']
	collision = parameters['collision']
	c = parameters['c']

	# Initialize the hash table
	hash_table = hashing.hash_table(hash_func=hash_func, mod=mod,
									bucket_size=bucket_size, collision=collision, 
									c=c)

	# Get ready to read input
	input_gen = None
	try:
		input_gen = fileIO.read_input(input_path)
	except FileNotFoundError:
		print(f"The provided input path, {input_path}. Could not be found. ", \
				"Please check your input and try again.")

	# Read into the hash table
	for elem in input_gen:
		hash_table.add(elem)

	# Record the output
	fileIO.write_outp(hash_table, output_path)
