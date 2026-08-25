# 1. Take two numbers as input and print their sum.
num1=float(input("Enter first number:"))
num2 =float(input("Enter second number:" ))
sum = num1 + num2
print(f'The sum of {num1} and {num2} is {sum}   ')

# 2. Convert temperature from Celsius to Fahrenheit.
celsius = float(input ('enter the temp in celsius:'))
fahrenheit = (celsius *9/5) + 32
print(f'The temperature in fahrenheit is {fahrenheit} ')

# 3. Swap two numbers without using a third variable.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num1, num2 = num2, num1
print(f'After swapping: the number1 is {num1}, and number2 is {num2}')

# 4. Check the type of different variables.
print(type(num1))

# 5. Convert "123" to an integer and multiply it by 5.

str_num ='123'
num1 = int(str_num)
result = num1 * 5
print(f'The result of multiplying {str_num} by 5 is {result}')