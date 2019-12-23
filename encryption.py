def encryption(s):
    sqrt = math.sqrt(len(s))
    floor = int(math.floor(sqrt))
    ceil = int(math.ceil(sqrt))
    answer = ""
    for j in range(100000):
        for i in range(j,len(s),ceil):
            answer = answer + s[i]
        answer = answer + " "
        if j+1 == ceil:
            break
    return answer
