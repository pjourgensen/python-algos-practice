"""
countTriplets takes in an array, arr, and an integer, r, and returns the number of
triplets of indices (i,j,k) such that the elements at those indices are geometric 
progressions of the ratio, r, and are ordered such that i < j < k.
"""

def countTriplets(arr, r):
    start = {}
    middle = {}                             #Maintain 2 dicts that hold counts of appearances of particular element
    total = 0

    for i in arr:
        prev = i/r
        if prev in middle:
            total += middle[prev]           #If prev is in middle, add appearances of prev in middle to total
        if prev in start:
            if i not in middle:
                middle[i] = 0
            middle[i] += start[prev]        #If prev is in start, add appearance of current element to middle
        if i not in start:
            start[i] = 0
        start[i] += 1

    return total
