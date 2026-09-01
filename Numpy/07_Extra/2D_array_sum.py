#  sum the values in a column of a 2d matrix

# axis =0, means sum along various row in a column - sum of column
# axis =1, means sum along various column in a row - sum of row

import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [8,9,10]])

result = np.sum(array)
print(result)

# sum the columns
results = np.sum(array, axis =0)
print(results)

# sum the columns
results = np.sum(array, axis =1)
print(results)


