#dictinoaries are used to store data in key value pairs, and they are unordered, changeable and indexed.

my_dict = {"name":"girdhari", "age":25, "city":"delhi", "is_student":True, "subject":["python", 'phys', 'chem']}
print(my_dict)

print(my_dict["name"]) #this will give you the value of the key "name"

# print(my_dict("phone")) #this will give you the value of the key "phone", if the key is not present in the dictionary, it will give you an error

print(my_dict.get("phone")) #this will give you the value of the key "phone", if the key is not present in the dictionary, it will give you an error

my_dict['phone']= 1234567890 #this will add a new key value pair in the dictionary
print(my_dict)

# updating the name key value pair in the dictionary
my_dict['name'] = 'Girdhari singh'

# adding a new key value pair in the dictionary using update() method
my_dict.update({"email":"girdhari@example.com"})
print(my_dict)

# updating multiple key value pairs in the dictionary using update() method
my_dict.update({"phone":"9876543210", "age":23})
print(my_dict)