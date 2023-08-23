# Task 2
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
if month_name == "January":
    days = 31
elif month_name == "February":
    days = 28
elif month_name == "March":
    days = 31
elif month_name == "April":
    days = 30
elif month_name == "May":
    days = 31
elif month_name == "June":
    days = 30
elif month_name == "July":
    days = 31
elif month_name == "August":
    days = 31
elif month_name == "September":
    days = 30
elif month_name == "October":
    days = 31
elif month_name == "November":
    days = 30
elif month_name == "December":
    days = 31
else:
    days = 0 # just to have an invalid input

if days != 0:
    print(month_name, "has", days, "days.")
else:
    print("Invalid month name. Please enter a valid month from the list")
