import random

def generate(path='student_input.txt', n=70):

	with open(path, 'w') as file:
		choices = random.choices(range(0, 99999), k=n)


		count = 0
		for choice in choices:
			file.write(str(choice) + "\n")

			count += 1

			if count > 4:
				file.write("\n")
				count = 0

if __name__ == '__main__':
	generate()