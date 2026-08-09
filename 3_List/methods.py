courses =['physics', 'chemistry', 'maths', 'english']

# #append an elemnt - it adds a new elemnts in the end of the list
# courses.append('biology')
# print(courses)

# #insert an element at a specific index
# courses.insert(1, 'history')
# print(courses)

# # #now suppose you have two list and you wana add the elemnts of one of the string to other --
# courses2 =['Arts', 'polity']
# # courses.insert(0,courses2) # this method will result in adding the list itself rather than the elements -- same thing with append
# # print(courses)
# # print(courses[0]) # this results in that list not an element

# # #to solve this problem we use extend

# courses.extend(courses2) # this method will add the elements of the list rather than the list itself -- adds in the end of the list
# print(courses)


# #removing elemnts from the list
# courses.remove('history') #this will remove the first occurrence of the element from the list
# print(courses)

# #another method to remove an element from the list is pop() method, it will remove the last element of the list if no index is provided, otherwise it will remove the element at the specified index
# courses.pop() #this will remove the last element of the list
# print(courses)
# popped = courses.pop() #this will remove the last element of the list and return it, returns the popped element
# print(popped)


# # reversing a list
# courses.reverse()
# print(courses)

# #sorting a list
# courses.sort() #this will sort the list in ascending order
# print(courses)
# #if we want to sort the list in descending order we can use the reverse parameter of the sort() method
# courses.sort(reverse=True) #this will sort the list in descending order
# print(courses)

# #if you want to sort your list and store it as a new list without altering the original list
# sorted_list = sorted(courses)
# print(courses) # this method doesnt alters the original list
# print(sorted_list)


# some maths on list
nums =[-1,4,2,3,5]
print(sum(nums))
print(min(nums))
print(max(nums))


# index finding in list

print(courses.index('chemistry'))


# check whether an element is present in the list or not
print('art' in courses) #print false boolean as art is not present in the list