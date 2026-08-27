import numpy as np
array = np.array([1,2,3])

# # some basic operations
# print(array -1)
# print(array +2)
# print(array *3)
# print(array/4)
# print(array//4)
# print(array**2)

# # some built in maths functions
# print (np.sqrt(array))
# second_array = np.array([1., 1.41421356, 1.73205081])
# print(np.round(second_array))
# print(np.pi)

#vectorised maths functions

radii = np.array([1,2,3])

# area of the circle
print(np.round(np.pi*radii**2))



# element wise arithemetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 // array2)
print(array1 ** array2)


# comparsion operators

print(array1 > array2)
print(array1 < array2)
print(array1 == array2)
print(array1 != array2)
print(array1 >= 2)

array1[array1<3] =0
print(array1)
