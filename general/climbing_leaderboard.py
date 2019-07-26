def climbingLeaderboard(scores, alice):
    """
    Find and return a list of leaderboard positions corresponding to each of 
    Alice's scores.
    Parameters:
    -----------
    scores: list
        Current leaderboard scores organized in descending order
    alice: list
        List of Alice's scores organized in ascending order
    Returns:
    --------
    alice_pos: list
        List of leaderboard positions corresponding to each of Alice's scores
    """
    scores_dict = {}
    pos = 1
    for i in scores:
        if i not in scores_dict:
            scores_dict[i] = pos
            pos += 1
    
    idx = 0
    alice_score = alice[idx]
    alice_pos = []
    for j in range(1,len(scores)+1):
        while scores[-j] > alice_score:
            alice_pos.append(scores_dict[scores[-j]]+1)
            idx += 1
            if idx == len(alice):
                return alice_pos
            alice_score = alice[idx]
    
    while idx < len(alice):
        alice_pos.append(1)
        idx += 1
    
    return alice_pos
