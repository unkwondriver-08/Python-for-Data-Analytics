# what is sys ?
# sys is a built-in module in Python that provides access to some variables used or maintained by the interpreter
# and to functions that interact strongly with the interpreter. It allows you to manipulate the Python runtime environment, 
# including command-line arguments, standard input/output, and system-specific parameters.

# when we write import sys, it imports the sys module and makes its functions and variables available for use in our code.
# when we write import  a module how does it know where to look for the module? -
#  so it checks in multiple locations in a specific order, these location are stored in a list called sys.path, which is a list of strings that specifies the search path for modules.
#  when we import a module, Python searches for the module in the sys

import sys
print(sys.path)  # printing the sys.path list, which contains the search path for modules   

# suppose we want to import a module from a different folder, but the folder is not in the sys.path list, 
# then we can add the folder to the sys.path list using sys.path.append() method.
import sys
sys.path.append('/path/to/folder')  # adding the folder to the sys.path list

# but the problem with this approach is that it is not a permanent solution, 
# because the sys.path list is reset every time we run the script, so we need to add the folder to the 
# sys.path list every time we run the script. also if we want to change any thing in the sys.path then we have to do manually at all locations where we are using the sys.path, so it is not a good approach.

# second approach is to set the PYTHONPATH environment variable, which is a list of directories that Python will search for modules.
# we can set the PYTHONPATH environment variable in the terminal or command prompt,