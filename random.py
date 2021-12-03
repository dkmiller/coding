"""Prints the entries in the array in a clockwise spiral, starting at the
entry [0][0] and moving inward. For example, if
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
then the output is 1 2 3 6 9 8 7 4 5.
"""
def print_spiral(arr):
    # The four directions East(E), South (S), West (W), and North (N)
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    # Maximal (and minimal) indices allowed in directions E, S, W, N.
    edge = [len(arr[0])-1,len(arr)-1,0,0]
    # Current coordinates, starting in upper left corner.
    position = (0,0)
    # Index of our starting direction.
    current = 0
    for _ in range(len(arr)*len(arr[0])): # Total number of entries to print
        (x, y) = position
        (a, b) = directions[current]
        e = edge[current]
        print(arr[x][y])
        if x*a == e*a and y*b == e*b: # Have reached an edge.
            edge[current-1] -= 1
            current = (current + 1) % 4
            (a, b) = directions[current]
        # Increment position by the current direction.
        position = (x+a,y+b)

"""Finds the longest substring with exactly M characters. For example, if
s = "aabbbcccbba", M = 2
then the result is "bbbcccbb".
Complexity: time = O(len(s)), space = O(M)
"""
def longest_substring(s, M):
    d = {} # Last occurance of characters in s[i]..s[j].
    i = 0 # Starting index of test substring.
    start, end = -1, -1 # Candidate return indices for start and end of string.
    for j, c in enumerate(s): # s[j] = c
        d[c] = j
        # We've found a new longest substring.
        if len(d) == M and j-i > end-start:
            start, end = i, j
        # Remove all occurances of first character from test substring.
        if len(d) > M:
            c = s[i]
            i = d[c] + 1
            del d[c]
    if start < 0:
        raise ValueError("Fewer than %d characters." % M)
    else:
        return s[start : end+1] # Returns s[start]..s[end].

"""Finds the longest common subsequence of two arrays.
"""
def longest_common_subsequence(xs, ys):
    pass

"""Finds the longest palindrome in a string.
"""
def longest_palindrome(s):
    # Center of the current palindrome. A "position" is either a character, the
    # space between two characters, or the left / right edge. So if s has length
    # n, there are 2*n+1 positions. Odd positions correspond to edges or spaces
    # between characters, even positions to characters themselves.
    center = 0 # Center of current palindrome.
    # Lengths of longest palinromes. lengths[p] stores the length (in number of
    #positions) of the longest palindrome at position p.
    lengths = []
    while center < 2*len(s)+1:
        left = center-1
        right = center+1
        while left % 2 != 0 or

        # Find largest palindrome centered at center.
        pass

""" Determines whether an array of relative indices is a
complete cycle. That is, if arr[i] == n, then arr[i]
points to arr[i+n], possibly modulo the length of the array.
A complete cycle is an array of relative indices such that
following the path hits all indices in a cycle. For example,
[1,1,1,1] is a complete cycle, but [1,-1,1,-1] is not.

This function returns True on empty arrays and False on null
arrays.
"""
def is_complete_cycle(arr):
    if arr is None:
        return False
    # Dictionary of indices that have been visited.
    visited = {}
    length = len(arr)
    # Next index to visit.
    next = 0
    # Walk through path given by relative indices.
    while next not in visited:
        visited[next] = True
        # Index pointed to by arr[next].
        next = (next + arr[next]) % length
    # Only a complete cycle if we’ve visited everything and are
    # pointing back at 0.
    return len(visited) == length and next == 0
