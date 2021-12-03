# Chapter 3 of Cracking the Coding Interview
# Stacks and Queues

# 3.1. Use a single array to implement three stacks.
# TODO: needs improvement.
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

# 3.2. A stack which also has a function min which returns 
# the minimum element. 
class MinStack:
    def __init__(self):
        self.elts = []
        self.mins = []
    def push(self, x):
        if len(self.elts) == 0:
            self.elts.append(x)
            self.mins.append(0)
        else:
            length = len(self.elts)
            old_loc = self.mins[-1]
            old_min = self.elts[old_loc]
            self.elts.append(x)
            self.mins.append(length if x < old_min else old_loc)
    def pop(self):
        self.mins.pop()
        return self.elts.pop()
    def min(self):
        return self.elts[self.mins[-1]]

# 3.3. Distributes a stack over a set of stacks with limited capacity.
class SetOfStacks:
	# Assume capacity > 0
	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = []
	def push(self, x):
		if len(self.stacks) == 0:
			self.stacks.append([])
			self.stacks[0].append(x)
		else:
			if len(self.stacks[-1]) == self.capacity:
				self.stacks.append([])
				self.stacks[-1].append(x)
			else:
				self.stacks[-1].append(x)
	def pop(self):
		result = self.stacks[-1].pop()
		if len(self.stacks[-1]) == 0:
			self.stacks.pop()
		return result
	# Assumes n < size / capacity.
	def popAt(self, n):
		pass