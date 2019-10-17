class hash_table:
	"""
	Constructor for hash table
	"""
	def __init__(self, bucket_size, mod, collision='quadratic', size=120):

		collisions = {'linear': self.linear, 'quadratic': self.quadratic, \
				'chaining': self.chaining}

		# check that parameters are okay
		assert(size > 0)
		assert(bucket_size > 0)
		assert(mod > 1)
		assert(collision in collisions.keys())

		# store the parameters for this table
		self.bucket_size = bucket_size
		self.mod = mod
		self.collision = collisions[collision]
		self.size = size
		
		
		# initialize the table
		# if bucket size > 1 table consists of empty lists
		if self.bucket_size > 1:
			return [list()] * self.size

		# otherwise table consists of Nones (emptys)
		else:
			return [None] * self.size

	def linear(self, hash_key):
		# keep track of probes
		count = 0

		# keep yielding hashes until we find a usable bucket
		new_hash = hash_key
		while count < self.size:
			new_hash = new_hash + 1 if new_hash + 1 < self.size else 0
			yield new_hash

		return
	
	def quadratic(self, hash_key):
		# keep track of probes (i)
		count = 0

		new_hash = hash_key
		while count < self.size:
			# let c1 = 0 and c2 = 1
			new_hash = (new_hash + count ** 2) % self.mod
			yield new_hash

		return

	def chaining(self, hash_key):
		# turn non-list buckets into lists as necessary
		if type(self.table[hash_key]) is not list:
			self.table[hash_key] = list(self.table[hash_key])
		
		return

	def class_hash(self, elem):
		hash_key = elem % self.mod

		# split function based on bucket size
		if self.bucket_size == 1:
			if self.collision is not self.chaining:
				if self.table[hash_key] is None:
					self.table[hash_key] = elem

				else:
					# probe for an empty bucket
					for p in collision(hash_key):
						if self.table[p] is None:
							self.table[p] = elem
							break

					l

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



class StorageException(Exception):
	def __init__:
