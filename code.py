# Chapter 2

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