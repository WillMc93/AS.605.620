

class hash_table:
	def __init__(self, size=120, bucket_size):
		self.size = size
		self.bucket_size = bucket_size
		self.table = self.init_table(size)

	def init_table(self):
		if self.bucket_size > 1:
			return [[None] * self.bucket_size] * self.size
		else:
			return [None] * self.size

	def linear(self, hash_key):
		if self.full is False:
			return hash_key + 1 if hash_key + 1 < self.size else 0
		else:
			raise StorageException()

	def quadratic(self, hash_key):
		return None

	def chaining(self, hash_key):
		return None

	def chlan_hash(self, elem, mod, collision=self.linear):
		hash_key = elem % mod

		if self.table[hash_key] is None:
			self.table[hash_key] = elem

		else:
			old = hash_key
			while self.table[hash_key] is not None:
				old = hash_key
				hash_key = collision(hash_key)

			self.table[hash_key] = elem


class StorageException(Exception)
