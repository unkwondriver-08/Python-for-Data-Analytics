# Conditionals & Loops

# # Print multiplication tables.

# i =1
# while i<5:
#     j=1
#     while j<11:
#         print(i*j)
#         j+=1
#     i+=1


# Print prime numbers from 1–100.

# num =2
# while num <=100:
#     i=2
#     is_prime = True
#     while i<num:
#       if  num%i == 0:
#         is_prime = False
#         break
#       i+=1

#     if(is_prime):
#        print(num)

#     num+=1


# # Find the factorial of a number.
# num = int(input('enter the number whose factorial you want: '))
# i=1
# product =1
# while i <= num:
#    product =product*i
#    i+=1
# print(product)

# Print Fibonacci numbers.
# # fibonacci series- each number is sum of past  2 numbers, 0 1 1 2 3 5 8

# num1 =0
# num2 =1
# print(num1)
# print(num2)
# upto =8
# sum =0
# while num2 <upto:
#     sum = (num1+num2)
#     num1 = num2
#     num2 = sum
#     print(num2)
 

# # Check if a number is an Armstrong number.

# num = int (input('please enter the number which you want to check: '))
# y =num
# n = len(str(num))

# new_list =[]
# while num > 0:
#    j = num%10 
#    new_list.append(j)
#    num =num//10

# i=0
# sum =0
# while i <n:
#    sum = sum + new_list[i]**n
#    i+=1

# if y == sum:
#    print (f"the given number {y} is a armstrong number")
# else:
#    print(f"the given number {y} is not a armstrong number")




# Find the GCD of two numbers.
# num = int(input("enter the number 1 for which you want to calculate the GCD: "))
# num2 = int(input("enter the number 2 for which you want to calculate the GCD: "))
# factor_num1 =set()
# factor_num2 =set()
# i=1
# j=1
# while num >= i:
#     if num%i==0:
#      factor_num1.add(i)
#     i+=1

# while num2 >= j:
#     if num2%j==0:
#      factor_num2.add(j)
#     j+=1

# print(f'the gcd of the number is {max(factor_num1.intersection(factor_num2))}')

# Print different star patterns.

num = int (input('enter the no of rows in star patten you need: '))

i =0

while i<num:
    j=0
    while j  <= i :
        print("*", end ='')
        j+=1
    print() # move the cursor to next line
    i+=1