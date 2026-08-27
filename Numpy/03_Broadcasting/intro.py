# Broadcasting allows numpy to perform operations on arrays with  different shapes by virtually expanding dimensions
# so they match the larger array's shape

# THE RULES
# The dimensions have the same size.
# OR
# One of the dimension has a size of 1

# eg shapes given: (3,3) and (3,3) | (3,3) and (1,1) both are same or one matches to be 1
# eg2 shapes given: (3,3) and (3,1) | (1,5) and (4,1) - out of 1 and 4 we have 1, again out of 5 and 1 we hve a 1


import numpy as np
array1 = np.array([[1,2,3]])
array2 = np.array([[1],
                  [2],
                   [3]])

print(array1.shape)
print(array2.shape)

print(array1 + array2)
# it was possible because out of the shape we have 1 as in each dimension