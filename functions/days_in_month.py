## Convert the is_leap() function
# First, function is_leap() return True if it is a leap year and return False if it is not a leap year
# Create a new function called days_in_month()
# You are then going to create a function called days_in_month() which will take a year and a month as inputs
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  
year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a Month: ")) # Enter a month
days = days_in_month(year, month)
print(days)