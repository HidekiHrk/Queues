from queues.errors import EmptyQueueError, FullQueueError

class Queue:
	def __init__(self, size=None):
		self.__data = []
		self.size = size

	def add(self, item):
		if self.size and len(self) >= self.size:
			raise FullQueueError("The queue is already FULL >:[")
		return self.__data.insert(0, item)

	def next(self):
		if len(self) == 0:
			raise EmptyQueueError("The queue is EMPTY :(")
		return self.__data.pop()

	def __next__(self):
		return self.next()

	@property
	def raw_values(self):
		return self.__data

	@property
	def values(self):
		return self.__data[::-1]

	def clear(self, quantity=0):
		if quantity == 0:
			self.__data = []
		else:
			self.__data = self.__data[:-quantity]
		return len(self.__data)

	def __len__(self):
		return len(self.__data)

	def __iter__(self):
		while len(self) > 0:
			yield self.next()
	
	def __repr__(self):
		return f"<{__name__}.{type(self).__name__} values: {len(self)}>"

	# <> >= <= comparators:

	def __lt__(self, other):
		return len(self) < len(other)

	def __gt__(self, other):
		return len(self) > len(other)

	def __le__(self, other):
		return len(self) <= len(other)

	def __ge__(self, other):
		return len(self) >= len(other)
