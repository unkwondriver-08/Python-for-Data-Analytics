a=[1,2,3]   
b=[1,2,3]

print(a==b)  # this statement will check if the value of the variable a is equal to the value of the variable b, if it is true, it will return True, otherwise it will return False

#  but checking for equals to and is are different, because equals to will check for the value of the variable, whereas is will check for the memory location of the variable.

print(a is b)  # this statement will check if the value of the variable a is the same object as the value of the variable b, if it is true, it will return True, otherwise it will return False


a=[1,2,3]   
b=a

print(a==b)  # this statement will check if the value of the variable a is equal to the value of the variable b, if it is true, it will return True, otherwise it will return False

print(a is b)  # this statement will check if the value of the variable a is the same object as the value of the variable b, if it is true, it will return True, otherwise it will return False

print(id(a))  # this statement will return the memory location of the variable a
print(id(b))  # this statement will return the memory location of the variable b    
print(id(a) == id(b))  # this is same as checking a is b; this statement will check if the memory location of the variable a is equal to the memory location of the variable b, if it is true, it will return True, otherwise it will return False