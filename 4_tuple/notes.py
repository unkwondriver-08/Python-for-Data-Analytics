#tuple is immutable data structure, we cant change the values of tuple once it is created. we can only access the values of tuple using indexing and slicing. we can also use tuple methods to perform operations on tuple.

##creating a tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) #this will print the tuple

# tuple1[0] = 10 #this will give an error because tuple is immutable
# print(tuple1) #this will print the tuple

# #accessing the values of tuple using indexing
print(tuple1[0]) #this will print the first value of the tuple
print(tuple1[1:4]) #this will print the values from index 1 to 3
print(tuple1[-1]) #this will print the last value of the tuple
print(tuple1[-3:-1]) #this will print the values from index -3 to -2
print(tuple1[::-1]) #this will print the values of the tuple in reverse order
print(tuple1[::2]) #this will print the values of the tuple at even index
print(tuple1[1::2]) #this will print the values of the tuple at odd index
print(len(tuple1)) #this will print the length of the tuple


#  you cant directly append elemnts in the tuple, hence to add the elements we can use
tuple = (1,3,4)
print(tuple)
tuple = tuple +(2,)
print(tuple)
print(tuple.sort)