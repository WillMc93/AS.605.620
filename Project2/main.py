import hashing
import fileIO
import sys
import re

DEFAULTS = {'input_path': '', 'output_path': './outputs/default_output.txt', \
						'hash_method': 'class', 'mod': 120, 'bucket_size': 3, \
						'collision': 'quadratic', 'c': [0,1]}

INT_PARAMS = ['mod', 'bucket_size']

# Regex patterns
param_pat = r'^--(?P<parameter>[A-Za-z_]+)=(?P<value>.+)$'
c_pat = r'^\[(?P<c1>[0-9]+.?[0-9]*),[\s]*(?P<c2>[0-9]+.?[0-9]*)\]&'
int_pat = r'[0-9]+'
str_pat = r'[A-Za-z0-9/\\._]+'


parameters = DEFAULTS.copy()

def help():
	print("Usage: main.py [input_path] [output_path] [hash_method] [mod]", \
				"[bucket_size] [collision] [c]")
	print("Arguments may be entered positionally as above, ", \
			"or with prefixes (e.g. --input_path=[path])")
	print("If using a named parameter all must be named ", \
			"(except for input and output which are checked for).")
	print("Default hash_method . . . c = 'class', '120', '3', ", \
		"'quadratic', [0,1]")
	print("\nOptions: ")
	print("\thash_method: choose between 'class' or 'student'")
	print("\tmod: mod value for class hash")
	print("\tbucket_size: size of buckets")
	print("\tcollision: 'linear' 'quadratic' or 'chaining'")
	print("\tc: c1 and c2 for quadratic in list i.e. [c1,c2]")

def parse(option):
	# Check option for parameter match
	match = re.fullmatch(param_pat, option)

	# Ooops, not valid
	if not match:
		print(f"Parameter, {option}, is not valid. This likely ", \
				"results in default behviour.")
		return None

	# Set the parameter
	else:
		param = match.group('parameter')
		value = match.group('value')

		if param not in DEFAULTS.keys():
			print(f"The parameter, {param}, is not a valid option. " \
					"This likely results in default behaviour.")
		
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
	if len(sys.argv) == 1:
		help()
		return

	if len(sys.argv) == 2 and sys.argv[1] == '--help':
		help()
		return

	if len(sys.argv) < 2:
		print(f"The program must be run with at least an input path, but ", \
				"no parameters were found. Check your command input ", \
				"and try again.")
		return

	# Check to see if input parameters are positional
	positional = True
	for elem in sys.argv[1:]:
		if '=' in elem:
			positional = False

	# If they are positional set our options
	if positional:
		parameters['input_path'] = sys.argv[1]
		
		if len(sys.argv) > 2:
			parameters['output_path'] = sys.argv[2]
		if len(sys.argv) > 3:
			parameters['hash_method'] = sys.argv[3]
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
		# Check for = mismatch on input (allowed)
		if '=' not in sys.argv[1]:
				parameters['input_path'] = sys.argv[1]
		# Check for = mismatch on output (allowed)
		if len(sys.argv) > 2 and '=' not in sys.argv[2]:
				parameters['output_path'] = sys.argv[2]

		# Set the named parameters. = mismatch not allowed from here on.
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

	return

if __name__ == '__main__':
	# Run the set parameters function. Takes care of all input parameters.
	set_params()

	# Unpack parameters
	input_path = parameters['input_path']
	output_path = parameters['output_path']
	hash_method = parameters['hash_method']
	mod = parameters['mod']
	bucket_size = parameters['bucket_size']
	collision = parameters['collision']
	c = parameters['c']

	# Initialize the hash table
	hash_table = hashing.hash_table(hash=hash_method, mod=mod,
									bucket_size=bucket_size, collision=collision, 
									c=c)

	input_gen = fileIO.read_input(input_path)

	# Run the hashtable
	for elem in input_gen:
		hash_table.hash(elem)

	# Record the output:
	fileIO.write_outp(hash_table, output_path)



