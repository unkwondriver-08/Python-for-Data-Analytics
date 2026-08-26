def hello_function():
    return "Hello, Function!"  # This function returns a string when called.

# the benifit of using return statement is that it allows us to capture the output of a function and use it later in the program,
# making our code more modular and reusable. whereas print statement is used to display output immediately and 
# does not allow us to capture the output for later use.

hello_function()  # Calling the function to execute its code, but not capturing the returned value.
print(hello_function())  # Calling the function and printing its return value directly, which is "Hello, Function!"

result = hello_function()  # Capturing the returned value in a variable
print(result)  # Printing the captured value, which is "Hello, Function!"   


# we can do multiple operations in a function and return the result of those operations.
print(hello_function().upper())  # Calling the function, converting the returned string to uppercase, and printing it.
print(hello_function().lower().upper())  # Calling the function, converting the returned string to lowercase, and printing it.
