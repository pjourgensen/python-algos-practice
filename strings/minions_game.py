"""
minion_game takes a string as input and determines whether Stuart or Kevin won the game
and what their is. Stuart scores points for every consecutive subsequence that begins
with a consonant, while Kevin scores points for every consecutive subsequence that
begins with a vowel. Outputs "Draw" if it is a tie.
"""

def minion_game(string):

    vowels = ['A','E','I','O','U']
    string_len = len(string)
    stuart_score = 0
    kevin_score = 0

    for idx in range(string_len):               #for every letter, check who will score points
        if string[idx] in vowels:
            kevin_score += string_len-idx       #points will equal string_len minus current index
        else:
            stuart_score += string_len-idx
    
    if stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    elif kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    else:
        print("Draw")
