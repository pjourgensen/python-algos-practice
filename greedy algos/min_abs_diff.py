"""
minimumAbsoluteDifference takes in an array and returns the minimum absolute difference 
of any 2 elements in the array. Begin by sorting array, then sequentially step through
pairs of the array.
"""

def minimumAbsoluteDifference(arr):
    arr.sort(reverse=True)
    min_diff = float('inf')
    for i in range(len(arr)-1):
        curr_diff = arr[i] - arr[i+1]
        if curr_diff < min_diff:
            min_diff = curr_diff
    return min_diff
