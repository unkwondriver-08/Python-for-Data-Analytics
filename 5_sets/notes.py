#sets are data structure, which dont care about the order of the values and also dont allow duplicate values. 
# we can perform various operations on sets like union, intersection, difference etc.

#the main benefit of using sets are - it doesnt store the duplicate values, so it is very useful when we want to store unique values.
# it is optimised to check whether a specific value is present in the set or not, 
# i.e it is very fast to check whether a value is present in the set or not. it is faster than list and tuple.

a_set = {1, 2, 3, 4, 5}
print(a_set)
print(2 in a_set)

b_set =(2,3,5,6,78)

#unique opearation on the sets

print(a_set.intersection(b_set)) # this gives the common values in the sets
print(a_set.difference(b_set))  #this gives the values which are present in a_set but not in b_set
print(a_set.union(b_set)) #this gives the values which are present in both the sets
