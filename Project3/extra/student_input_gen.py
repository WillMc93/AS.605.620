import random

def generate(path='student_input.txt', samples=4, n=64):

	nucleotides = ['A', 'T', 'G', 'C']

	with open(path, 'w') as file:
		
		for i in range(samples):
			choices = random.choices(range(0, 4), k=n)
			file.write("String=")

			for choice in choices:
				file.write(str(nucleotides[choice]))

			file.write("\n")


if __name__ == '__main__':
	generate()