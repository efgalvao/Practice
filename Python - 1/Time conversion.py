"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
"""
from datetime import datetime

def timeConversion(s):
    hora = datetime.strptime(s, "%I:%M:%S%p")
    return hora.strftime("%H:%M:%S")
    

print(timeConversion('07:05:45PM'))