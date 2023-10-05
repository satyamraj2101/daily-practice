# Write a Python program to calculate the number of days between two dates.
from datetime import date 
day1 = int(input("Enter the date :"))
month1 = int(input("Enter the month :"))
year1 = int(input("Enter the year :"))
day2 = int(input("Enter the date :"))
month2 = int(input("Enter the month :"))
year2 = int(input("Enter the year :"))

date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)
result = date2 - date1
print(result)