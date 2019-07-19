"""
maxMin takes in an integer, k, and an array of integers, arr. It returns the minimum difference
of the maximum and minimum values of all subarrays of length k of arr. Greedy component comes
from sorting the array at the beginning before marching through and measuring the difference
of the first and last values of the sequential subarrays.
"""

def maxMin(k, arr):
    arr.sort() 
    min_unfairness = float('inf')
    for i in range(len(arr)-k+1):
        curr_unfairness = arr[(i+k)-1] - arr[i]
        if curr_unfairness < min_unfairness:
            min_unfairness = curr_unfairness
    
    return min_unfairness
