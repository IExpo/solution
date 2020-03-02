def climbingLeaderboard(scores, alice):
    ans=""
    for i in range(len(alice)):
        for s in range(len(scores)): 
            if scores[s] > alice[i]:
                pass
            else:
                scores.insert(s,alice[i])
                break
        if s+1==len(scores):
            scores.append(alice[i])
        ans = ans + count_ans(scores,alice[i])
    return ans

def count_ans(scores,alice):
    x=0
    index=1
    while scores[x] != alice:
        if scores[x] == scores[x+1]:
            pass
        else:
            index = index+1
        x=x+1
    return str(index)
