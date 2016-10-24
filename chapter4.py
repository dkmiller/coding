# Chapter 4. Trees and graphs

# 4.1. Checks if a tree is balanced.
def isBalanced(root):
	working = [(root, 0)]
	lengths = {}
	while len(inProg) > 0:
		(current,count) = working.pop()
		if len(current.children) > 0:
			for child in current.children:
				working.append((child,count+1))
		else:
			lengths[count] = True
			if len(lengths) > 2:
				return False
			l1, l2 =  lengths.keys()[0], lengths.keys()[1]
			if abs(l1-l2)>2:
				return False
	return True

# 4.2. Checks if there is a path between two nodes in a
# directed graph. Doesn't assume the graph is connected.
def isPath(start, end):
	done = set()
	do = set([start])
	while len(do) > 0:
		v = do.pop()
		if v not in done:
			done.add(v)
		if end in done:
			return True
		for u in v.edges:
			if u not in done and u not in do:
				do.add(u)
	return False

# 4.3. Given a sorted (increasing order) array, returns a
# binary tree with minimal height.
def array_to_tree(arr):
	def att_bounds(arr, low, high):
		if high - low == 0:
			return Node(arr[low])
		elif high - low == 1:
			root = Node(arr[high])
			root.left = Node(arr[low])
			return root
		elif high - low == 2:
			root = Node(arr[low+1])
			root.left = Node(arr[low])
			root.right = Node(arr[high])
			return root
		else:
			mid = (high-low+1)/2
			root = Node(arr[mid])
			root.left = att_bounds(arr,low,mid-1)
			root.right = att_bounds(arr, mid+1,high)
			return root
	return att_bounds(arr, 0, len(arr)-1)
