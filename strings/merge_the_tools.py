"""
merge_the_tools takes a string and an integer, k, as inputs. k must be a factor of the length
of the string as the string is divided into equal subsequences of length k. The subsequences 
are then pruned of repeated characters and printed out on individual lines.
"""

def merge_the_tools(string, k):

    idx = 0
    while idx < len(string):
        t = string[idx:idx+k]
        u = ''
        for char in t:
            if char not in u:
                u += char
        print(u) 
        idx+=k
