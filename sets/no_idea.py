"""
no_idea takes in an array and two sets, A and B, and outputs a 'happiness' score.
If an element of the array is in A, happiness goes up 1, but if the element is in
B, happiness goes down 1. Inputs are read from stdin.
"""

import os
import sys
import re

def no_idea(arr,A,B):
    happiness = 0
    for entry in arr:
        if entry in A:
            happiness += 1
        if entry in B:
            happiness -= 1
    return happiness


if __name__ == '__main__':
    n,m = tuple(map(int,input().rstrip().split()))
    arr = list(map(int,input().rstrip().split()))
    A = set(map(int,input().rstrip().split()))
    B = set(map(int,input().rstrip().split()))

    print(no_idea(arr,A,B))
