"""
hash_table takes care of storing, maintaining, and interacting with
the hash table.

@authour Will McElhenney
@date 11/6/2019
"""
class hash_table:
	"""
	Constructor for hash table

	@param size: integer for the size of the table
	@param mod: integer for the class modulo hash function
	@param bucket_size: integer for the size of the buckets
	@param collision: string for the collision method to be used
	@param c: c values for quadratic collisions
	@param hash_func: string for class hash or student hash
	"""
	def __init__(self, size=120, mod=120, bucket_size=1, collision='quadratic', \
						c=[0.5,0.5], hash_func='class'):

		# dictionary of accepatable collision types, mapped to the proper func.
		collisions = {'linear': self.linear, 'quadratic': self.quadratic, \
							'chaining': self.chaining}

		# dictionary of accptable hash types, mapped yadda-yadda
		hashes = {'class': self.class_hash, 'student': self.my_hash}

		# Store the parameters for this table iff acceptable, default otherwise
		self.size = size if size > 0 else 120
		self.bucket_size = bucket_size if bucket_size > 0 else 1
		self.mod = mod if mod > 1 else 120
		
		self.prim_coll_count = 0 # collision count
		self.unplaced = [] # items that couldn't be added
		self.entered = 0 # number of items entered into the table
		

		# Tell user if we defaulted
		if size <= 0:
			print(f"Given size, {size}, is not valid. Defaulting to 120.")
		if bucket_size <= 0:
			print(f"Given bucket size, {bucket_size}, is not valid. ", \
				"Defaulting to 3.")
		if mod <= 1:
			print(f"Given mod, {mod}, is not valid. Defaulting to 120")


		# Initialize collision and c
		self.collision = None
		self.c = list()

		# Error check and set collision and c
		if collision in collisions.keys():
			self.collision = collisions[collision]
			self.c = c

		else:
			# Tell user what we're defaulting
			print(f"The specified collision method {collision} is not valid. ", \
					"Defaulting to Quadratic with c=[0.5,0.5]")

			# Default
			self.collision=self.quadratic
			self.c = [0.5,0.5]
		
		
		# Initialize the table
		self.table = list()
		# if bucket size == 1 (and not chaining) table consists of empty of Nones
		if self.bucket_size == 1 and self.collision != self.chaining:
			self.table = [None] * self.size

		# otherwise table consists of empty lists unless chaining
		elif self.bucket_size > 1 and self.collision != self.chaining:
			self.table = [list() for _ in range(self.size)]

		elif self.collision == self.chaining:
			self.table = [self.link() for _ in range(self.size)]

		# Initialize freespace stack for chaining
		self.freespace = None
		if self.collision == self.chaining:
			self.freespace = [i for i in range(self.size)]			

		# Set the hash function (class vs mine)
		self.hash_func = None
		if hash_func in hashes.keys():
			self.hash_func = hashes[hash_func]
		else:
			print(f"The hash-type, {hash_type}, is not valid. Defaulting to ", \
					"the in-class hash.")
			self.hash_func = self.class_hash

	"""
	Internal link object for "node" in chained hash
	"""
	class link:
		"""
		Constructor

		@param value: value to be entered into hash_table
		@param next_link: int representing the index of the next link
		"""
		def __init__(self, value=None, next_link=None):
			self.value = value
			self.next_link = next_link

	"""
	Function for calculating how full table is
	"""
	def fill_ratio(self):
		return self.entered / (self.size * self.bucket_size)

	"""
	Linear probing function

	@param hash_key: hash key originally generated
	"""
	def linear(self, hash_key):
		# keep track of probes
		count = 0

		# keep yielding hashes until we find a usable bucket
		new_hash = hash_key
		while count < self.size:
			count += 1
			new_hash = new_hash + 1 if new_hash + 1 < self.size else 0

			yield new_hash

		if count == self.size:
			yield None

		return
	
	"""
	Quadratic probing function. 
	Could be combined with linear, but it was messy when I tried.

	@param hash_key: hash key originally generated
	"""
	def quadratic(self, hash_key):
		# keep track of probes (i)
		count = 0

		# keep yielding hashes until we find a useable bucket
		new_hash = hash_key
		while count < self.size:
			count += 1
			c1, c2 = self.c
			new_hash = (new_hash + c1 * count + c2 * count**2) % self.mod
			

			yield int(new_hash)

		if count == self.size:
			yield None

		return

	"""
	Chaining collision function. Maintains free space in self.freespace, and 
	updates previous link in chain.

	@param hash_key: hash key originally generated
	"""
	def chaining(self, hash_key):
		# linear probe for space but make reference in link
		count = 0

		assert(self.freespace != None)

		# if table is full skip all this
		if len(self.freespace) < 1:
			return None

		new_hash = hash_key
		occupant = self.table[hash_key]

		# Traverse the chain of already collided entries
		while occupant.next_link != None:
			new_hash = occupant.next_link
			occupant = self.table[new_hash]

		# Pop Next Free Slot off stack
		new_hash = self.freespace.pop()
		occupant.next_link = new_hash

		return new_hash

	"""
	Function to add items to the hash table. Tries to put the item in by calling
	the hash function, but if it can't it calls the probing function.

	Could be neater. 

	@param elem: value to be added to the hash table
	"""
	def add(self, elem):
		hash_key = self.hash_func(elem)

		# split function based on bucket size
		if self.bucket_size == 1:
			# split bucket_size == 1 on chaining
			if self.collision != self.chaining:
				# if empty, place here
				if self.table[hash_key] is None:
					self.table[hash_key] = elem

				# otherwise, probe for an empty bucket
				else:
					for p in self.collision(hash_key):
						# increment collision count
						self.prim_coll_count += 1

						# if hash found and empty, place here
						if p is not None and self.table[p] is None:
							self.table[p] = elem
							break

						# otherwise if no hash was found (table full)
						elif p is None:
							self.unable.append(elem)
							self.prim_coll_count -= 1 # last one don't count
							break


			# special case for chaining
			else:
				# if empty place here and remove freespace entry
				if self.table[hash_key].value is None:
					self.table[hash_key].value = elem
					self.freespace.remove(hash_key)

				else:
					# increment collision counter
					self.prim_coll_count += 1

					# find a hash
					hash_key = self.collision(hash_key)

					# if suitable hash was found place it
					if hash_key is not None:
						self.table[hash_key].value = elem
					else:
						self.unplaced.append(elem)

		# bucket size > 1
		else:
			# if space in this bucket, place here
			if len(self.table[hash_key]) < self.bucket_size:
				self.table[hash_key].append(elem)

			# otherwise, search for hash
			else:
				for p in self.collision(hash_key):
					self.prim_coll_count += 1

					# if p is not None and there is room in this bucket
					if p is not None and len(self.table[p]) < self.bucket_size:
						self.table[p].append(elem)
						break

					# uh-oh
					elif p is None:
						self.prim_coll_count -= 1 # last one don't count
						self.unplaced.append(elem)
						break

		self.entered += 1

	"""
	class_hash is the default hash function

	@param elem: value to be added to the hash table
	"""
	def class_hash(self, elem):
		return elem % self.mod

	"""
	my_hash is the hash I provide. It is riff on middle-square hashing, 
	technically a type of multiplicative hashing.

	@parm elem: value to be added to the hash table
	"""
	def my_hash(self, elem):
		# middle-square
		hash_key = str(elem**2)

		# if result is too big
		if len(hash_key) > len(str(self.size)):
			cut = len(hash_key) - len(str(self.size))

			if cut % 2 == 0:
				cut = int(cut / 2)
				hash_key = hash_key[cut:]
				hash_key = hash_key[:-cut]
			else:
				ceil = int((cut - 1)  / 2)
				floor = int((cut + 1) / 2)
				hash_key = hash_key[ceil:]
				hash_key = hash_key[:-floor]

			assert(len(hash_key) <= 3 and len(hash_key) > 0)

		# fit to table
		# Here's where I had to get a little creative. Because the table is
		# short and includes {11} we have to fit the middle-square to the table
		if len(hash_key) == len(str(self.size)):
			if int(hash_key) > self.size:
				temp = int(hash_key)

				if temp > self.size:
					temp = temp % self.size

				hash_key = str(temp)

		return int(hash_key)

	"""
	Function to produce a string representation of the table.
	"""
	def to_string(self, nothing=5):
		# string we'll output later
		outp = str()

		# counter for keeping the number of entries per line
		prints = 0

		# typed this one too many times
		_nothing = "-" * nothing

		# takes prints and outp from the loop and gives it an increment and a
		# newline if need be
		def _next_line(prints, outp):
			prints += 1
			if prints > 4:
				outp += "\n"
				prints = 0

			return prints, outp

		# returns appropriate amount of space for length of given value
		def _fill(value):
			return " " * (len(_nothing) - len(str(value)))

		# Split on bucket size and chaining strat
		if self.bucket_size == 1 and self.collision != self.chaining:
			for bucket in self.table:
				if bucket == None:
					outp += _nothing
				else:
					outp += _fill(bucket) + str(bucket)

				outp += " "

				prints, outp = _next_line(prints, outp)

		# if we didn't use chaining and our bucket size > 1
		elif self.bucket_size > 1 and self.collision != self.chaining:
			for i in range(self.size):
				outp += str(i) + _fill(i)

				if len(self.table[i]) == 0:
					outp += (_nothing + " ") * 3

				else:
					for elem in self.table[i]:
						outp += _fill(elem) + str(elem) + " "

					fill = self.bucket_size - len(self.table[i])
					outp += (_nothing + " ") * fill

				outp += "\n"

		# if we did use chaining
		elif self.collision == self.chaining:
			for bucket in self.table:
				if bucket.value == None:
					outp += _nothing
				else:
					outp += _fill(bucket.value) + str(bucket.value)

				outp += " "

				prints, outp = _next_line(prints, outp)

		return outp