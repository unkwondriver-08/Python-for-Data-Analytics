# loops allows us to run across the values in a data structure
numbers =[1,2,3,4,5]
# for item in numbers:
#     print(item)

# now if we wana find a specific number or run upto a specific position then break running the loop, then we can use BREAK

for items in numbers:
    if items ==3:
       print("found")
       break
    print(items)


# now if we wana skip a specific number or skip a specific position then continue running the loop, then we can use CONTINUE

for items in numbers:
    if items ==3:
       print("found")
       continue
    print(items)


# nested loops

for items in numbers:
    for len in "abc":
       for values in ",..":
        print(items, len, values)