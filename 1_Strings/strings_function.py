message = "this is A string"

# print(message.lower()) #this converts the string to lowercase
# print(message.upper()) #this converts the string to uppercase
# print(message.title()) #this converts the first letter of each word to uppercase

# help(str) #this will give you all the methods that can be used with strings
# dir(message) #this will give you all the methods that can be used with strings

print(len(message)) #this will give you the length of the string
print(message.count('s')) #this will give you the count of a specific character in the string
print(message.find('s')) #this will give you the index of the first occurrence of a specific character in the string strating from 0 as first index
print(message.rfind('s')) #this will give you the index of the last occurrence of a specific character in the string
note = 'if there is no match, find will return -1'
print(note)