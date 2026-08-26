#slicing the rows

import numpy as np
array = np.array([[1,2,3,15],
                  [4,5,6,12],
                  [7,8,9,10],
                  [10,11,12,14]])
# print(array)

# syntax array[start:end:step]
# start is inclusive and end is inclusive
print(array[1,1])

# print everything
print(array[0:])

print(array[1:5])
# Start at row 1 and go up to, but not including, row 5; if row 5 doesn't exist, stop at the end.

# print from specific row to specific row
print(array[1:6]) #whatever you write in the end, you will get upto the end only, if the no crosses no of rows

# print in between
print (array [0:3])

# skip means - Move forward by n step at a time, so when skip =1 it will skip only one row every time
# print with skip
print(array [0:3:1]) # to find the next row Move forward by 1 step at a time, 

print(array [0:5:2]) # at every time it will move forward by 2 rows which means, current and one after it

print (array[::2]) # select all and print every second row

print(array[::-2]) #prints in reverse order to every second row