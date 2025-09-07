class Stack:
	def __init__(self):
		self.data = []

	def push(self, item):
		"""
		push: Adds an item to the end of the collection
		"""
		# your code here
		self.data.append(item)

	def pop(self):
		"""
		pop: Removes the last item from the collection and returns it
		"""
		# your code here
		if len(self.data) <= 0:
			print("Stack Underflow")
			return False
		else:
			popped_item = self.data[-1]
			self.data.pop(-1)
			return popped_item
		

	def peek(self):
		"""
		peek: Observes the last item in the collection without removing it
		"""
		# your code here
		if len(self.data) <= 0:
			print("Stack Underflow")
		else:
			return self.data[-1]

	def is_empty(self):
		
		"""
		is_empty: Returns whether the stack is empty or not (boolean)
		"""
		# your code here
		print(self.data)
		if self.data:
			return False
		else:
			return True


"""
Main
"""
stack = Stack()

print('is_empty:', stack.is_empty())
stack.push('A')
stack.push('B')
stack.push('C')
print('peek:', stack.peek())
print('pop:', stack.pop())
print('peek', stack.peek())
print('is_empty:', stack.is_empty())

