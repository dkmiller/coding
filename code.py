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
    result = root
    while node.next != None:
        if i < n:
            i += 1
        else:
            result = result.next
        node = node.next
    if i < n:
        return None
    else:
        return result.value