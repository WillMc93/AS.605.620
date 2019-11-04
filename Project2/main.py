import hashing
import fileIO
import sys

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print(f"The program must be run with a input path and an output ", \
				"path, but we only found one path. Check your input ",
				"and try again")

	input_path = sys.argv[1]
	output_path = sys.argv[2]
	hash_func = 'class'

	if len(sys.argv) > 3:
		hash_func = sys.argv[3]


	