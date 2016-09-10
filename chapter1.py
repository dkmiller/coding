# Chapter 1

# 1.1. Returns true if and only if the string has unique characters
def has_unique_characters(string):
    appeared = {}
    for c in string:
        if c in appeared:
            return False
        else:
            appeared[c] = True
    return True

# 1.2. Reverses an array with a null object at the end.
def reverse(arr):
    if arr == None:
        return None
    l = 0 # Number of non-null elements.
    while arr[l] != None:
        l += 1
    for i in range(l/2):
        temp = arr[i]
        arr[i] = arr[l-1-i]
        arr[l-1-i] = temp
    return arr