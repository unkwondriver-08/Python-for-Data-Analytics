user ='admin'
logged_in = True

if user == 'admin' and logged_in:  # this statement will check if the value of the variable user is equal to "admin" and the value of the variable logged_in is True, if both conditions are true, the code inside the if block will be executed
    print("Welcome admin")
else:
    print("You are not admin")

logged_in = False
if user == 'admin' or logged_in:  # this statement will check if the value of the variable user is equal to "admin" or  the value of the variable logged_in is True, if both conditions are true, the code inside the if block will be executed
    print("Welcome admin")
else:
    print("You are not admin")

if user == 'admin' and not logged_in:  # this statement will check if the value of the variable user is equal to "admin" and the value of the variable logged_in is False, if both conditions are true, the code inside the if block will be executed
    print("Welcome admin")
else:
    print("You are not admin")