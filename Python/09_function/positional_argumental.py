# what is positional argumental?
# Positional arguments are a type of argument that is passed to a function based on the order in which they are defined in the function's parameter list.
#  When you call a function, the values you provide are assigned to the parameters in the order they are defined.

# but what if we want to pass the arguments in a different order?
# In that case, we can use keyword arguments, which allow us to specify the parameter names along with their corresponding values when calling the function. 
# This way, we can pass the arguments in any order we like. for example, if we have a function that takes two parameters, we can call it like this:
def greet_user(name, age):
    print(f"Namaste!", name, "your age is", age)
greet_user(age=25, name="Girdhari singh")  # Calling the function with keyword arguments, which allows us to pass the arguments in any order

# what is arg, and kwargs?
# *args and **kwargs are special syntax in Python that allow you to pass a variable(as many as u want) number of arguments to a function.

# *args allows you to pass a variable number of positional arguments to a function. 
# For example, if you have a function that takes two parameters, but you want to allow the user to pass in any number of additional arguments, you can use *args like this:
def greet_user(name, *args):        
    print(f"Namaste!", name, "your age is", args)
greet_user("Girdhari singh", 25, "male", "India")  # Calling the function with a variable number of positional arguments, which will be collected into a tuple called 'args'
#  it is positional argument because we are passing the arguments in the order they are defined in the function's parameter list.
#  we can't pass it like this greet_user(25, "Girdhari singh", "male", "India") because it will throw an error because the first argument is expected to be a string, but we are passing an integer.



# **kwargs allows you to pass a variable number of keyword arguments to a function. it is similar to *args, but instead of collecting the arguments into a tuple, it collects them into a dictionary.
# it is also positional argument because we are passing the arguments in the order they are defined in the function's parameter list.
# For example, if you have a function that takes two parameters, but you want to allow the user to pass in any number of additional keyword arguments, you can use **kwargs like this:
def greet_user(name, **kwargs):
    print(f"Namaste!", name, "your age is", kwargs)
greet_user("Girdhari singh", age=25, gender="male", country="India")  # Calling the function with a variable number of keyword arguments, which will be collected into a dictionary called 'kwargs'
#  it is keyword argument because we are passing the arguments with their corresponding parameter names.

# what is a docstring?
# A docstring is a special type of string that is used to document a function, class, or module in Python. 
# It is a string literal that appears as the first statement in a function, class, or module definition, and 
# it is used to provide information about the purpose and behavior of the code. -- it is also called documentation string.
# it is just like a comment, but it is more formal and structured. it is used to provide information about the purpose and behavior of the code.
