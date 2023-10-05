# Write a Python program that prints the calendar for a given month and year.
import calendar
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

date = calendar.month(year , month)
print("Calender  : ")
print(date)
