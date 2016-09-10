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
        print arr[x][y]
        if x*a == e*a and y*b == e*b: # Have reached an edge.
            edge[current-1] -= 1
            current = (current + 1) % 4
            (a, b) = directions[current]
        # Increment position by the current direction. 
        position = (x+a,y+b)