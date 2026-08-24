# find the no of days in a month, also make sure for the leap year february has 29 days.
month_days= [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    return (year%4==0 and year%100!=0 or year%400==0)

def no_ofdays(month, year):
    if month<1 or month>12:
        return "Invalid month"
    if month ==2 and leap_year(year):
        return 29
    else:
        return month_days[month]

# print(no_ofdays(2, 2020))  # Output: 29 (2020 February has 29 days in a leap year)
