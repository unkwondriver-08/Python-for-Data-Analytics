# function: It allows us to write a block of code that can be reused multiple times in a program.
# Functions help in breaking down complex problems into smaller, manageable parts, making the code more organized and easier to read. 
# They can take inputs (parameters), perform specific tasks, and return outputs (results). 
# Functions are defined using the 'def' keyword followed by the function name and parentheses.

def hello_world():
    print("Hello, World!") #this is a simple function that prints "Hello, World!" when called.

hello_world() # calling the function to execute its code


# what happens if we define a function and dont pass any operation to it, then it will return None by default.
def empty_function():   
    pass  # 'pass' is a placeholder that does nothing. It allows us to define an empty function without any operation.

empty_function()  # calling the function to execute its code

# what happens if we define a function and dont pass any operation to it and dont write pass also
def another_empty_function():
    # This function does not have any operation or 'pass' statement.
    # In Python, if a function does not have any code, it will return None by default.
 return None  # explicitly returning None to indicate that the function does not perform any operation.

another_empty_function()  # calling the function to execute its code, it does not perform any operation and returns None by default.

print(another_empty_function())  # calling the function and printing its return value, which is None


# what if we print the function name without parentheses, it will return the function object itself, not the result of the function execution.
print(another_empty_function)  # This will print the function object, not the return value.


# DRY principle: "Don't Repeat Yourself" is a software development principle that emphasizes the importance of reducing code duplication.