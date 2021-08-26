from collections import defaultdict

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

# 1.4. Decides if two strings are anagrams or not.
def are_anagrams(s1, s2):
    char_count = defaultdict(int)
    for c in s1:
        char_count[c] += 1
    for c in s2:
        char_count[c] -= 1
    for c in char_count:
        if char_count[c] != 0:
            return False
    return True

# 1.6. Rotates an NxN matrix in place.
def rotate(mat):
    N = len(mat)
    for i in xrange(N/2):
        for j in xrange(N-2*i-1):
            temp = mat[i][i+j]
            mat[i][i+j] = mat[N-1-i-j][i]
            mat[N-1-i-j][i] = mat[N-1-i][N-1-i-j]
            mat[N-1-i][N-1-i-j] = mat[i+j][N-1-i]
            mat[i+j][N-1-i] = temp
    return mat
