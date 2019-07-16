"""
luckBalance takes in an integer, k, and a 2d array, contests. Contests is a list of element pairs,
whose first element denotes a quantity of 'luck' needed to win a particular contest and whose
second element is a binary variable indicating if contest is 'important' or not. Contests that are
lost add to one's 'luck balance', while contests that are won detract from it. K denotes the maximum 
number of important contests that can be lost. This function determines the maximal 'luck balance'
that can be achieved accordingly.
"""

def luckBalance(k, contests):
    contest_dict = {1:[],0:[]}                      #Separate important and unimportant contest
    
    for pair in contests:
        if pair[1] == 0:
            contest_dict[0].append(pair[0])
        else:
            contest_dict[1].append(pair[0])
    
    luck_balance = sum(contest_dict[0])             #No need to win any unimportant contests
    contest_dict[1].sort(reverse=True)              #Sort by contests requiring more luck first
    
    if k >= len(contest_dict[1]):
        luck_balance += sum(contest_dict[1])        #If you can lose all important contests, do so
    else:
        luck_balance += sum(contest_dict[1][:k])    #Else, lose the contests requiring the most luck
        luck_balance -= sum(contest_dict[1][k:])    #Win the contests requiring the least luck
    
    return luck_balance
