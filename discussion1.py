import math

def gen_masks(n):
	# generate the masks

	# start w/ binary 1 (01)
	# it's important that this starts with False becasue we really only need half the possiblities
	masks = [[False, True]]

	# create binary numbers of length n
	for i in range(2, n):
		# need to store the generated masks separately temporarily
		new_masks = []

		# for each already generated mask
		for mask in masks:
			if len(mask) == i:
				# for each mask of the current length
				# add the succeeding even number: current mask + a zero (False) at the end
				even_mask = mask + [False]

				# add the succedding odd number: mask + a one (True) at the end
				odd_mask = mask + [True]

				# store in temporary space
				new_masks.append(even_mask)
				new_masks.append(odd_mask)

		# add temporary space to persistent space
		masks += new_masks

	# remove the all-true mask (last one)
	masks = masks[:len(masks) - 1]
				
	# prepend the correct number of False's to the shorties
	prepd_masks = []
	for mask in masks:
		prepend = [False for _ in range(n - len(mask))]

		prepd_masks.append(prepend + mask)

	return prepd_masks

def min_diff(array):
	# get the array masks
	# (we really only need the first half of the returns here)
	masks = gen_masks(len(array))

	# get half the sum of the array
	array_sum = 0
	for a in array:
		array_sum += a
	half_sum = array_sum / 2

	# stat variables
	min_diff = float('inf')
	part_mask = []

	for mask in masks:
		# get the masked array
		masked_array = apply_mask(array, mask)

		# get the complementary array
		comp_array = apply_mask(array, complement(mask))

		diff = abs(sum(masked_array) - sum(comp_array))
		
		if diff < min_diff:
			min_diff = diff
			part_mask = mask
		
	return min_diff, part_mask

def apply_mask(array, mask):
	# return an list consisting of the 
	return [array[i] for i in range(len(array)) if mask[i] == True]

def complement(mask):
	# return the complement of the mask (101 -> 010)
	return [not x for x in mask]
		
def report(array, diff, mask):

	part1 = apply_mask(array, mask)
	part2 = apply_mask(array, complement(mask))

	# print the info
	print(f"The lowest difference in the disjoint sets was found to be: {diff}")
	print(f"Partition 1: {part1}")
	print(f"Partition 2: {part2}")


if __name__ == '__main__':
	array = [1,2,3,4,5,6]
	array2 = [1,2,3,6]

	import random
	array_rand = random.sample(range(30), 16)
	

	# Test 1
	outp = min_diff(array)
	report(array, *outp)

	# Test 2
	outp = min_diff(array2)
	report(array2, *outp)

	# Test 3
	outp = min_diff(array_rand)
	report(array_rand, *outp)
