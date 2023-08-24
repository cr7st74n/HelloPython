# This is a sample Python script.
import datetime

print("Hello!  Can I ask your name and the month that you were born ?")
name = input("Name: ")

month = input("Month: ")
month.capitalize()

nameNumber = len(name.strip())

currentMonth = datetime.datetime.now().strftime('%B')  # I found this way to get the current month in text

# Conditional
if month == currentMonth:
    print(' "Happy Birthday month" :D !')
else:
    print("It's not your birthday yet :)")

print(f'Welcome to class {name} and your birthday will be in {month}')

print(f'The number of letters in your name is {nameNumber} ')

