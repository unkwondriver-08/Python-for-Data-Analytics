dicti ={"name":"girdhari", "age":25, "city":"delhi", "is_student":True, "subject":["python", 'phys', 'chem'], "email":"girdhari@example.com "}
print(dicti)

# deleting a key value pair from the dictionary using del keyword
del(dicti["age"]) #this will delete the key value pair with the key "age"
print(dicti)

email = dicti.pop("email") #this will delete the key value pair with the key "email" and return the value of the key "email"
print(dicti)
print(email)

print(len(dicti))