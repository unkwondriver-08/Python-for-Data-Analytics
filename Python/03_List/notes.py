
COURSES = ['PYTHON', 'JAVA', 'C++', 'JAVASCRIPT', 'HTML', 'CSS']

#first and last element of the list
print(COURSES[0]) #this will give you the first element of the list
print(COURSES[-1]) #this will give you the last element of the list     

# accessing elemnts of the list
print(COURSES[0:4]) #this will give you the elements from index 0 to index 3, that mean including starting index, and dont include last index
print(COURSES[:2]) #this will give you the first two elements of the list
print(COURSES[2:]) #this will give you the elements from index 2 to the end of the list
print(COURSES[::2]) #this will give you every second element of the list strarting form index 0
print(COURSES[::3]) #this will give you every third element of the list starting from index 0

#reverse the list
print(COURSES[::-1]) #this will give you the list in reverse order