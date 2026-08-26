# accessing columns and rows together
import numpy as np
array = np.array([[1,2,3,15],
                  [4,5,6,12],
                  [7,8,9,10],
                  [10,11,12,14]])


# print the first two rows and first two columns  # LAST VALUE IS NON EXCLUSIVE
print(array[0:2,0:2])

# print the first two rows and its last two columns
print(array[0:2, 2:4])

# print the last two rows and its last two columns
print(array[2:4,2:4])