# we can define function where user must need to pass some arguments to the function, otherwise it will throw an error.

def greet_user(name):  # 'name' is a parameter that the function expects to receive
    print(f"Hello, {name}!")  # using the parameter 'name' to greet the user with string hello
greet_user("Girdhari singh")  # Calling the function with an argument, which will print "Hello, Girdhari singh!"

# If we call the function without an argument, it will throw a TypeError:
# greet_user()  # This will result in a TypeError: greet_user() missing 1 required positional argument: 'name'

# writinga function with a default argument, so that if user does not pass any argument then it will take the default value.
def greet_user(name, age = "not specified"):  # 'age' is a parameter with a default value of "not specified"
    print(f"Namaste!", name, "your age is", age)  # using the parameters 'name' and 'age' to greet the user with string hello
greet_user("Girdhari singh")  # Calling the function with only the 'name' argument
