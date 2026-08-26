# accesing the columns



import numpy as np
array = np.array([[1,2,3,15],
                  [4,5,6,12],
                  [7,8,9,10],
                  [10,11,12,14]])

# # select a element
# print([1,1])

# # print a specific column - we first need to select the row which we want and then we decide the column
# print(array[:, 1:4]) #select column from index 1 before index 4 in  all rows(:,) 

# # print every second column starting from column 0 in all rows
# # first choose the row and then choose the slicing format
# print(array[:, 0::2])

# print in the reverse order
print(array[:,::-1]) # every row and column, where the column order is in reverse order

# print in reverse order starting from column1

print(array[:,1::-1])

# print in reverse order starting fron last column
print(array[:,4::-1])