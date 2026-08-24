# standard library is a collection of modules and packages that come with Python, 
# and it provides a wide range of functionality for various tasks, such as file I/O, data manipulation, networking, and more. 
# The standard library is included with Python, so you don't need to install anything separately to use it.

import random
numbers = [1, 2, 3, 4, 5]
random_num = random.choice(numbers)  # using the choice() function from the random module to select a random number from the list

import math
result = math.sqrt(16)  # using the sqrt() function from the math module to calculate the square root of 16 
print(result)  # printing the result, which is 4.0

import datetime
import calendar

today_date = datetime.date.today()  # using the today() function from the date class in the datetime module to get the current date
print(today_date)  # printing the current date

print(calendar.isleap(2020))  # using the isleap() function from the calendar module to check if 2020 is a leap year, which will return True

import os 
current_directory = os.getcwd()  # using the getcwd() function from the operating system module to get the current working directory
print(current_directory)  # printing the current working directory

print(os.__file__)  # printing the file path of the os module, which shows where the module is located in the Python installation in our system. this is useful for debugging and understanding how Python modules are organized and where they are located in the file system.