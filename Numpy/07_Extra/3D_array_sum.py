# sum in a 3d arrray
# axis=0, sum of various 2d arrray
# axis=1, sum along various rows in each arrray
# axis=2, sum along various columns in each arrray
import numpy as np

array = np.array([[[1,2,3],
                  [4,5,6],
                  [8,9,10]],
                  [[1,2,3],
                  [4,5,6],
                  [8,9,10]]])
print(array.shape)

# sum of each matrix 
result = np.sum(array, axis =0)
print(result)

# sum along different rows of each matrix = sum of columnar element of each matrix
result = np.sum(array, axis =1)
print(result)

# sum along different columns of each matrix = sum of rows element of each matrix
result = np.sum(array, axis =2)
print(result)