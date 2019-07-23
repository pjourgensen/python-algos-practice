"""
findAnagrams takes in a string, s, and outputs the total number of anagrams
that exist among all of the different substrings of s.
"""

def findAnagrams(s):
    s_len = len(s)
    total = 0
    substr_dict = {}                                  #Create dict of sorted substrings
    for start in range(s_len):
        end = start+1
        while end <= s_len:
            substr = ''.join(sorted(s[start:end]))
            if substr in substr_dict:                 #Maintain count of how many times substring has appeared
                total += substr_dict[substr]
                substr_dict[substr] += 1
            else:
                substr_dict[substr] = 1
            end += 1
    return total
