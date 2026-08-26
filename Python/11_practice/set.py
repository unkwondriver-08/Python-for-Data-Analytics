# Sets

set1 = {"key", "lock", 1}
set2 = {"door", "house", 1}

# Find the union of two sets.

print(set1.union(set2)) # method 1

union_set= set1 | set2 #  mehtod 2
print(union_set)

union_set1 = set1.copy() # method 3
for num in set2:
    if num not in union_set1:
        union_set1.add(num)
print(union_set1)

# Find the intersection.

print(f"the intersection of set1 and set2 is {set1.intersection(set2)}")

# Find the difference.
print(f"the difference of set1 and set2 is {set1.difference(set2)}")

# Remove duplicates from a list using a set.
setc = set()
list_given =[1,1,1,2,3,2,3]

for num in list_given:
    setc.add(num)
print(setc)

