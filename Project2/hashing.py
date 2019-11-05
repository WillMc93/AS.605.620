class hash_table:
	"""
	Constructor for hash table
	"""
	def __init__(self, size=120, mod=120, bucket_size=3, collision='quadratic', \
						c=[0,1], hash='class'):

		# dictionary of accepatable collision types, mapped to the proper func.
		collisions = {'linear': self.linear, 'quadratic': self.quadratic, \
							'chaining': self.chaining}

		# dictionary of accptable hash types, mapped yadda-yadda
		hashes = {'class': self.hash, 'student': self.hash}

		# Store the parameters for this table iff acceptable, default otherwise
		self.size = size if size > 0 else 120
		self.bucket_size = bucket_size if bucket_size > 0 else 3
		self.mod = mod if mod > 1 else 120


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
					"Defaulting to Quadratic with c=[0,1]")

			# Default
			self.collision=self.quadratic
			self.c = [0,1]
		
		
		# Initialize the table
		self.table = list()
		# if bucket size > 1 table consists of empty lists
		if self.bucket_size > 1:
			self.table = [list() for _ in range(self.size)]

		# otherwise table consists of Nones (emptys)
		# we take care of chaining in the chaining function
		else:
			self.table = [None] * self.size

		# Set the hash function (class vs mine)
		if hash in hashes.keys():
			self.hash = hashes[hash]
		else:
			print(f"The hash-type, {hash_type}, is not valid. Defaulting to ", \
					"the in-class hash.")
			self.hash = self.class_hash


	def linear(self, hash_key):
		# keep track of probes
		count = 0

		# keep yielding hashes until we find a usable bucket
		new_hash = hash_key
		while count < self.size:
			new_hash = new_hash + 1 if new_hash + 1 < self.size else 0
			count += 1

			yield new_hash

		return
	
	def quadratic(self, hash_key):
		# keep track of probes (i)
		count = 0

		# keep yielding hashes until we find a useable bucket
		new_hash = hash_key
		while count < self.size:
			# let c1 = 0 and c2 = 1
			c1, c2 = self.c
			new_hash = (new_hash + c1 * count + c2 * count**2) % self.mod
			count += 1

			yield new_hash

		return

	def chaining(self, hash_key):
		# turn non-list buckets into lists as necessary
		if type(self.table[hash_key]) is not list:
			temp = self.table[hash_key]
			self.table[hash_key] = [temp]
			yield hash_key
		
		return

	def hash(self, elem):
		hash_key = elem % self.mod

		# split function based on bucket size
		if self.bucket_size == 1:
			if self.collision is not self.chaining:
				if self.table[hash_key] is None:
					self.table[hash_key] = elem

				else:
					# probe for an empty bucket
					for p in self.collision(hash_key):
						if self.table[p] is None:
							self.table[p] = elem
							break

			# special case for chaining
			else:
				self.collision(hash_key)
				self.table[hash_key].append(elem)

		# bucket size > 1
		else:
			if len(self.table[hash_key]) < self.bucket_size:
				self.table[hash_key].append(elem)

			else:
				for p in self.collision(hash_key):
					if len(self.table[p]) < self.bucket_size:
						self.table[p].append(elem)
						break

	def my_hash(self, elem):
		return

	def to_string(self):
		# string we'll output later
		outp = str()

		# counter for keeping the number of entries per line
		prints = 0

		# typed this one too many times
		_nothing = "-" * 5

		# didn't want to have type this over and over
		# this isn't the best solution, probably
		def _next_line(prints, outp):
			prints += 1
			if prints > 4:
				outp += "\n"
				prints = 0

			return prints, outp

		# Split on bucket size and chaining strat
		if self.bucket_size == 1 and self.collision is not self.chaining:
			for bucket in self.table:
				if bucket == None:
					outp += _nothing
				else:
					outp += str(bucket)

				outp += " "

				prints, outp = _next_line(prints, outp)

		# if we did use chaining
		elif self.collision is self.chaining:
			for bucket in self.table:
				if len(bucket) == 0:
					outp += _nothing + " "
					
					prints, outp = _next_line(prints, outp)

				else:
					for elem in bucket:
						outp += str(elem) + " "

						prints, outp = _next_line(prints, outp)

		# if we didn't use chaining and our bucket size > 1
		elif self.bucket_size > 1:
			for i in range(self.size):
				outp += str(i) + " " * 4

				if len(self.table[i]) == 0:
					outp += (_nothing + " ") * 3

				else:
					for elem in self.table[i]:
						outp += str(elem) + " "

					fill = self.bucket_size - len(self.table[i])
					outp += (_nothing + " ") * fill

				outp += "\n"

		return outp