# under what conditions the if statement will be false?
# conditions that will make the if statement false are:
# 1. if the condition is False 
# 2. if the condition is None
# 3. if the integer value is 0
# 4. if you put condition to an empty string, list, tuple, sets, dictionaries

condition =0

if condition:
    print("this is true")
else:
    print("this is false")

condition =()

if condition:
    print("this is true")
else:
    print("this is false")

condition ={}

if condition:
    print("this is true")
else:
    print("this is false")

condition =[]

if condition:
    print("this is true")
else:
    print("this is false")

condition =False

if condition:
    print("this is true")
else:
    print("this is false")

condition =None

if condition:
    print("this is true")
else:
    print("this is false")
    