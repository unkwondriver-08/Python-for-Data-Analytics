# Functions
# Write a function to check for a prime number.
def prime_number( num):
    i=2
    isprime = True
    
    if num ==1:
        print("not prime")
    if num ==2:
        print('prime')
    if num >2:
        while i<num:
            if num%i ==0:
                isprime = False
                break
            i+=1

    if(isprime):
        print("prime")
    else:
        print ('not prime')

num = int(input('tell the number you want to check whether a prime or not: '))
prime_number(num)
# Write a calculator using functions.
# Write a palindrome function.
# Write a leap year function.
# Write a function that returns the second largest element in a list.