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