# Chapter 2 of Cracking the Coding Interview
# Linked lists.

# Self-contained implementation of linked list.
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        n = self
        result = ""
        while n != None:
            result += str(n.value) + ", "
            n = n.next
        return "[" + result + "]"

    def append(self, value):
        end = Node(value)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def delete(self, value):
        n = self
        if value == n.value:
            return n.next
        while n.next != None:
            if n.next.value == value:
                n.next = n.next.next
                return self
            n = n.next


# Problem 2.1.
# Removes duplicates in a linked list.
def remove_duplicates(root):
    repeats = {}
    n = root
    repeats[n.value] = 1
    while n.next != None:
        if n.next.value in repeats:
            n.next = n.next.next
        else:
            repeats[n.next.value] = 1
            n = n.next

# Problem 2.2.
# Returns the n-th to last value in a linked list.
def to_last(root, n):
    i = 1
    node = root
    while i < n:
        node = node.next
        if node == None:
            return None # Error, the list is too short.
        i += 1
    result = root
    while node.next != None:
        result = result.next
        node = node.next
    return result.value


# Problem 2.3.
# Deletes a node in the middle of a linked list.
def delete(node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next
    else: # Degenerate case: node is end of the list.
        pass

# Problem 2.4.
# Adds two base-ten numbers stored as linked lists.
def add_linked(root1, root2):
    remainder = (root1.value + root2.value) / 10
    root = Node((root1.value + root2.value) % 10)
    node = root
    n1, n2 = root1.next, root2.next
    while n1 != None or n2 != None:
        v1 = 0 if n1 == None else n1.value
        v2 = 0 if n2 == None else n2.value
        remainder = (v1 + v2 + remainder) / 10
        value = (v1 + v2 + remainder) % 10
        node.next = Node(value)
        node = node.next
        n1 = n1.next if n1 != None else None
        n2 = n2.next if n2 != None else None
    if remainder > 0:
        node.next = Node(remainder)
    return root

# Problem 2.5.
# Finds the beginning of a loop in a circular linked list by
# implementing Floyd's cycle-finding algorithm.
def find_loop(root):
    if root is None:
        return None
	fast = root
    slow = root
    while fast != slow:
        if slow is None:
            return None
        slow = slow.next
        if slow is None:
            return None
        fast = fast.next.next
    slow = root
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow
