from queues.errors import EmptyQueueError

class Queue:
	def __init__(self, arr=[]):
		self.__data = arr

	def add(self, item):
		return self.__data.insert(0, item)

	def __next__(self):
		if len(self) == 0:
			raise EmptyQueueError("The queue is EMPTY >:[")
		return self.__data.pop()

	@property
	def values(self):
		return self.__data

	def clear(self, quantity=0):
		if quantity == 0:
			self.__data = []
		else:
			self.__data = self.__data[:-quantity]
		return len(self.__data)

	def __len__(self):
		return len(self.__data)
	
	def __repr__(self):
		return f"<{__name__}.{type(self).__name__} values: {len(self)}>"