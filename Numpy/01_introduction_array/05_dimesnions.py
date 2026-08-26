# dimensions of arary

import numpy as np

array0 = np.array ('A') #its a 0 dimension array
print(array0.ndim)  #ndim tells the dimesnion of the array


array1 = np.array (['A','B','C']) #its a 1 dimension array
print(array1.ndim)
print(array1.shape)


array2 = np.array ([['A','B','C'],
                    ['E','F','G']]) #its a 2 dimension array
print(array2.ndim)
print(array2.shape)


array3 = np.array ([[['A','B','C'],['E','F','G']],
                    [['g','H','I'],['J','K','L']]]) #its a 3 dimension array, IT HAVE DEPTH(LAYERS), ROWS, AND COLUMNS
print(array3.ndim)
print(array3.shape) # it have 2 layers, each layer have 2 rows and each row has 3 columns

# we can find a specific position elemnets in this way
# normal python way of doing this is called CHAIN INDEXING
print(array3[0][0][1])

# NUMPI GIVES US MULTIDIMENSIONAL INDEXING - FASTER THAN CHAIN
print(array3[0,0,1])

word = array3[0,1,1] + array3[1,0,1]+array3[1,1,1]
print(word)