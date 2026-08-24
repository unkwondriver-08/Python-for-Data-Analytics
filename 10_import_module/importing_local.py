# importing a local module
# it allows us to use the functions and variables defined in the module (this folder) in our current script.

from importlib import import_module

import example

no_of_days =example.no_ofdays(3, 2023) # calling the function from the imported module
print(no_of_days)


# importing a module from a different folder
# we can also import a module from a different folder, but we need to make sure that the folder is in the same directory as our current script, or we need to provide the full path of the module.
# importing from other folder only works if the folder name is proper, for example if module name is 3_import_module then we can't import it because it is not a valid module name, 
# so we need to rename the folder to a valid name, for example import_module_3.
#  we can also write from list_3 import add_num

# importing specfic function from a module -- but this limits our ability to use other functions from the module, so it is better to import the whole module and then use the function we need.

from example import no_ofdays
no_of_days = no_ofdays(2, 2020) # calling the function from the imported module
print(no_of_days)

# we can also alias the imported module name for making it shorter to call
from example import leap_year as ly
is_leap =ly(2020)
print(is_leap)

# import example.no_ofdays as nod will give an error because we can't import a function from a module using the dot notation, 
# we can only import the whole module or a specific function from the module.
# this is read as import a submodule from a module, but in our case no_ofdays is not a submodule, it is a function, so we can't import it using the dot notation.

from example import no_ofdays as nod, leap_year as ly
no_of_days = nod(2, 2020) 
print(no_of_days)
is_leap =ly(2020)   
print(is_leap)