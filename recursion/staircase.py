"""
stepPerms takes in a staircase height, n, and returns the number of ways the staircase
can be ascended taking 1, 2, or 3 steps at a time. Memoization is applied to speed up 
processing on sucessive queries.
"""

look_up_table = [0,1,2,4]

def stepPerms(n):
    if n < len(look_up_table):
        return look_up_table[n]
    else:
        current = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3) % 10000000007
        look_up_table.append(current)
        return current 
