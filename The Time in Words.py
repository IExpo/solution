def getHours():
    hour = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"
    }
    return hour

def getMinute():
    minute = {
        0 : "o' clock",
        15: "quarter",
        30 : "half",
        45: "quarter",
        1: "one minute",
        2: "two minutes",
        3: "three minutes",
        4: "four minutes",
        5: "five minutes",
        6: "six minutes",
        7: "seven minutes",
        8: "eight minutes",
        9: "nine minutes",
        10: "ten minutes",
        11: "eleven minutes",
        12: "twelve minutes",
        13: "thirteen minutes",
        14: "fourteen minutes",
        16: "sixteen minutes",
        17: "seventeen minutes",
        18: "eighteen minutes",
        19: "nineteen minutes",
        20: "twenty minutes",
        21: "twenty one minutes",
        22: "twenty two minutes",
        23: "twenty three minutes",
        24: "twenty four minutes",
        25: "twenty five minutes",
        26: "twenty six minutes",
        27: "twenty seven minutes",
        28: "twenty eight minutes",
        29: "twenty nine minutes",
    }
    return minute


def timeInWords(h, m):
    hour = getHours()
    minute = getMinute()
    if m == 0:
        return hour[(h)] + " " + minute[(m)]
    if m >= 1 and m <= 30:
        return minute[(m)] + " past " +  hour[(h)]
    else:
        m = 60-m
        return minute[(m)] + " to " +  hour[((h%12)+1)]
