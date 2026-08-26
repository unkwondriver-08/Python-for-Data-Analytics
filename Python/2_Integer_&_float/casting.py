num1 =100
num2 = "200.5"


#print(num1+num2) #this will give you an error because we cannot add an integer and a string

#to add an integer and a string, we need to convert the string to an integer or a float -- this method is called casting
print(num1+float(num2)) #this will give you the sum of the two variables

#you can't cast a float to an integer if the float has a decimal part(even if decimal part is 0), it will give you an error

print(str(num1)+' '+num2) #this will give you the concatenation of the two variables