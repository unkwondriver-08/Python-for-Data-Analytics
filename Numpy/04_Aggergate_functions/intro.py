# Aggergate functions = summarize data and typically returns a single value


import numpy as np

array = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])

print(np.sum(array))
print(np.min(array))
print(np.max(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.argmin(array)) #what is the position of the minimum value in array
print(np.argmax(array))


print(np.sum(array,axis=0)) #sum the value in the columns
print(np.sum(array,axis=1)) #sum the value in the rows