my_details ={"name":'girdhari', 'class':"7th semester"}

# this is an inccorrect method looping in this, because this will only print the keys not the values
for values in my_details:
    print(values)

# for writing with key value pair, you need to write it differently
for key, values in my_details.items():
        print(key, ":" ,values)