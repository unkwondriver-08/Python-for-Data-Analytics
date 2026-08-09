COURSES = ['PYTHON', 'JAVA', 'C++', 'JAVASCRIPT', 'HTML', 'CSS']

# # printing the courses using a for loop, where each item in the list is printed on a new line
# for item in COURSES:
#     print(item)

# # if you wana print the index of the item along with the item itself, you can use the enumerate() function, which returns both the index and the item
# for index, items in enumerate(COURSES):
#     print(index,items)

#we can also give starting value in the enumerate() function, which will be the starting index of the items in the list
for index, items in enumerate(COURSES, start=1):
    print(index, items  )
    print(f"{index}: {items}") # this is another way to print in more cleaner manner
#  here f stands for format, and it allows us to use variables inside the string by using curly braces {}