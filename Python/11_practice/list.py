# Lists
number = [1,1,2,3,4,5,6]
# # Find the largest element.

# print (f'the largest number in the list is {max(number)}')

# # Find the second largest element.
# number.sort(reverse=True)
# print(f"the second larget number in the list is {number[1]}")

# Remove duplicates.
# i = 0
# while i < (len(number)-1):
#     if number[i] == number[i+1]:
#         number.remove(number[i])
#     else:
#         i += 1

# print(number)

# # Reverse a list.
# reverse_string = number[::-1]
# print(reverse_string)

# # Count even and odd numbers.
# even_count =0
# odd_count =0

# for num in number:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print(f'the no of even number in list is {even_count} and the no of odd count is  {odd_count}')


# # Merge two lists.

# number2 = [7,8,9,10]
# print(number + number2)

# Remove all negative numbers.
i =0
# number3 =[-11,22,44,-9,55,4]
# while i < (len(number3)):
#     if number3[i]<0:
#         number3.remove(number3[i])
#     else:
#         i+=1
# print (number3)
# Find common elements of two lists.
# common_elemnt =[]
# number4 =[1,2,5,6]
# for num in number:
#     if num in number4:
#         common_elemnt.append(num)
#         i+=1
#     else:
#         i+=1
# print(common_elemnt)
# Rotate a list by one position.
# rotating by n means you are sending first n elemnt in the end and then appending the rest?

# new_list=[]
# n=2 #no of position by which rotate, 
# i=n
# # take last n elements from index n in the starting 
# while i <len(number):
#     new_list.append(number[i])
#     i+=1
# # take first n-1 element in the end
# i=0
# while i <n:
#     new_list.append(number[i])
#     i+=1
# print(new_list)

# Sort without using sort() (after you've learned algorithms).
number = [5, 2, 8, 1]
i = 0

while i < len(number):
    j = 0

    while j < len(number) - 1:
        if number[j] > number[j + 1]:
            number[j], number[j + 1] = number[j + 1], number[j]

    j += 1

    i += 1

print(number)