from math import log
from datetime import datetime, date

n = int(input())
dates = []

year = 2022
days_dif = []

for x in range(0, n, 1):
    inp = input().split(" ")
    dates.append([[inp[0], inp[1]], [inp[2], inp[3]]])

    if ((datetime.strptime(dates[x][0][0], "%b")).month > (datetime.strptime(dates[x][1][0], "%b")).month):
        year = 2021
    if ((datetime.strptime(dates[x][0][0], "%b")).month == (datetime.strptime(dates[x][1][0], "%b")).month and int(dates[x][0][1]) > int(dates[x][1][1])):
        year = 2021
    d1 = date(year, (datetime.strptime(dates[x][0][0], "%b")).month, int(dates[x][0][1]))
    d2 = date(2022, (datetime.strptime(dates[x][1][0], "%b")).month, int(dates[x][1][1]))  
    days_dif.append(d2-d1)

for days in days_dif:
    print("%0.3f" % (365 - 365 * log(days.days + 1, 365)))