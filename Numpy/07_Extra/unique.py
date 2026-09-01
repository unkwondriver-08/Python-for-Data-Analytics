import numpy as np
data = np.array([1,1,2,3,2,3,32,2])

print(np.unique(data)) #only prints the unique elements
print(np.unique(data, return_counts=1)) #this also tells the count of each element occured - count of 1, 2 etc as array