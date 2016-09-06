# Chapter 3 of Cracking the Coding Interview
# Stacks and Queues

# 3.1. Use a single array to implement three stacks.
class Stack3:
	def __init__(self):
		self.array = []
		self.indices = [0,0,0]
	# Pushes obj onto the i-th stack, i = 0, 1, 2
	def push(self, i, obj):
		self.array.insert(i + 3*self.indices[i], obj)
		self.indices[i] += 1
	# Pops the i-th stack.
	def pop(self, i):
		result = self.array[self.indices[i]]
		self.array[self.indices[i]] = None
		self.indices[i] -= 1
		return result