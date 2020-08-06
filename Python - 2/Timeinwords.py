"""
https://www.hackerrank.com/challenges/the-time-in-words/
"""
def timeInWords(h, m):
    numbers = {0:"o' clock", 1:'one',	2:'two', 3:'three', 4:'four', 5:'five',	6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',	12:'twelve', 13:'thirteen',	14:'fourteen', 15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two',	23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six', 27:'twenty seven', 28:'twenty eight', 29:'twenty nine', 30:'half'}
    hour = numbers[h]
    if (m < 15 and m > 1) or (m > 15 and m < 30):
        minu = numbers[m]
        return (f'{minu} minutes past {hour}')
    elif m == 1:
        minu = numbers[m]
        return (f'{minu} minute past {hour}')
    elif m == 15:
        return (f'quarter past {hour}')
    elif m == 30:
        return(f'half past {hour}')
    elif (m < 45 and m > 31) or (m > 45):
        minu = numbers[abs(60 - m)]
        hour = numbers[h + 1]
        return (f'{minu} minutes to {hour}')
    elif m == 45:
        hour = numbers[h + 1]
        return (f'quarter to {hour}')
    elif m == 31:
        minu = numbers[abs(60 - m)]
        hour = numbers[h + 1]
        return (f'{minu} minute to {hour}')
    elif m == 0:
        return (f'{hour} o\' clock')

print(timeInWords(5, 45))