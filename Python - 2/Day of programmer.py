import datetime 
"""
    https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
def dayOfProgrammer(year):
    days = 255
    if year < 1918 and year % 4 == 0:
        days -= 1
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days += 1
    elif year == 1918:
        days += 13
    year = datetime.date(year, 1, 1)
    data = year + datetime.timedelta(days)
    data = data.strftime("%d.%m.%Y")
    return(data)

print(dayOfProgrammer(1812))
# 1812 - 12/09
