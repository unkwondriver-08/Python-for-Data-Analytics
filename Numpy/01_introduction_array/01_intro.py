
import numpy as np
print(np.__version__)

# benifit of using the nupmy over the python eg:

my_list =[1,2,3,4]
# suppose you wana multiply each element with 2 then in py if you do
print(my_list*2) #instead of multplying with 2 it will duplicate the list

# hence numpy is more usefull because it allow more flexiblity over mathmatical operation with numbers

my_array = np.array(my_list)
print(my_array*2) #this will multiply each with 2

my_new = np.array([2,3,4,5])
print(type(my_new))
print(my_new.shape) #tells the no of rows and column in the array