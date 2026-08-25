# Tuples -- can't change the position and the elements in it
my_tuple = (1,2,4,5,6,1,2)
# Count occurrences of an element.
num = int( input("which number occurence you would like to count: "))
count =0
i=0
for number in my_tuple:
    if number == num:
        count+=1
        i+=1
    else:
        i+=1
print(f"the no of times {num} occur in the given tuple is {count}")
# Find maximum and minimum values.

print(f'the maximum value in the tuple is {max(my_tuple)}')
print(f'the minimum value in the tuple is {min(my_tuple)}')

# Convert a tuple to a list and vice versa.

tuple_to_list =[]
for num in my_tuple:
    tuple_to_list.append(num)
print(f"the list formed from the given tuple is {tuple_to_list} and its type is {type(tuple_to_list)}")
print(len(tuple_to_list))


list_to_tuple =()
for nums in tuple_to_list:
    list_to_tuple= list_to_tuple + (nums,)
print(f"the tuple formed from the given tuple is {list_to_tuple} and its type is {type(list_to_tuple)}")
print(len(list_to_tuple))
