# if else statements allows us to check for conditions and execute code based on whether the condition is True or False.

if True:  # this statement will always be true, so the code inside the if block will be executed
    print("This is true")

if False:  # this staement will always be false, so the code inside the if block will not be executed
    print("This is false")

langauge =  "python"

if langauge == "python":  # this statement will check if the value of the variable langauge is equal to "python", if it is true, the code inside the if block will be executed
    print("This is python")
elif langauge == "java":  # this statement will check if the value of the variable langauge is equal to "java", if it is true, the code inside the elif block will be executed
    print("This is java")
else:  # this statement will be executed if the above two conditions are false
    print("This is not python or java")

# does python have a switch case statement? 
# No, python does not have a switch case statement, but we can use if else statements to achieve the same functionality.
# however, in python 3.10 and above, we can use match case statement to achieve the same functionality as switch case statement.

# what is benifit of using switch case statement over if else statements?  
# The main benefit of using switch case statement over if else statements is that it is more readable and easier to understand, especially when we have multiple conditions to check.
