#  Lesson 11: The Math, Datetime, and Calendar Modules – All-in-One Example File

# 🔹 1. Using the math Module

import math

print("🔸 math Module Examples")

print("Square root of 16:", math.sqrt(16))
print("Power: 2 raised to 3 =", math.pow(2, 3))
print("Value of pi:", math.pi)
print("Ceil of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("Absolute value of -7:", math.fabs(-7))
print("Factorial of 5:", math.factorial(5))
print("Log base 10 of 1000:", math.log10(1000))
print("Sin(0):", math.sin(0))
print("Cos(0):", math.cos(0))

# 🔹 2. Using the datetime Module

import datetime

print("🔸 datetime Module Examples")

# Current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Only date
today = datetime.date.today()
print("Today's date:", today)

# Creating a custom date
dob = datetime.date(2000, 1, 15)
print("My date of birth:", dob)

# Getting individual parts
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)

# # 🔹 3. Using the calendar Module

import calendar

print("🔸 calendar Module Examples")

# Print full calendar of a year
print("Calendar of 2025:")
print(calendar.calendar(2025))

# Print a single month
print("Calendar for May 2025:")
print(calendar.month(2025, 5))

# Check if year is leap
print("Is 2024 a leap year?", calendar.isleap(2024))
print("Is 2025 a leap year?", calendar.isleap(2025))

# Count leap years between 2000 and 2030
print("Leap years between 2000 and 2030:", calendar.leapdays(2000, 2031))

