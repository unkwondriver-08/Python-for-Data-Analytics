# some important points
# while concatninating, we have to make sure that shape except the axis along which we are concatnating should be same
# suppose A and B have shape (2,3) and (3,3) now if we are concatnating along axis =0 then last element has to be same i.e 3,3
# axis =0, means no of rows will increase and stack along the column - thats why no of columns must be same
# 


import numpy as np

# 2s array concatination
array1 = np.array([[1,2,3],
                  [8,9,10]])

array = np.array([[1,2,3],
                  [8,9,10]])

# combine arrays
combined = np.concatenate((array1, array))
print(combined)

# tacks the arrays vertically. Or # concatenate along axis 0 (vertically)
combined = np.concatenate((array1, array),axis =0)
print(combined)

#joins the arrays horizontally. Or # concatenate along axis 1 (horizontally)
combined = np.concatenate((array1, array),axis =1)
print(combined)