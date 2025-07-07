'''
You are given a date. Your task is to find what the day is on that date.

Input

A single line of input containing the space separated month, day and year,
respectively, in MM DD YYYY format.

08 05 2015
Output

Output the correct day in capital letters.

WEDNESDAY
'''
from calendar import weekday

def cal(day):
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    week_no = weekday(year=int(day[2]),day=int(day[1]),month=int(day[0]))
    # print(week_no)
    print(week[week_no].upper())


# print(weekday(year=2015,day=5,month=8))
intp = input().split()
cal(intp)
# print(intp)