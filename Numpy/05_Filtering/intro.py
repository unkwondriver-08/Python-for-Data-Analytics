import numpy as np

ages = np.array([[21,17,19,20,16,30,18,65],[39,27,2,34,99,10,20,11]])

teenagers =ages[ages <18]
print(teenagers)

adults = ages[ages>18]
print(adults)

adult = ages[(ages>18) & (ages<65)]  #numpy follows some cpp so (and) wouldnt work here, so we use & and for OR we ise |
print(adult)

adult = ages[(ages>18) | (ages<65)]
print(adult)

senior = ages[ages>=65]
print(senior)

even = ages[ages%2==0]
print(even)


# while filtering if you want to preserve teh original array we need to use the where function

# bboolean methods flatten the array, but this method of using the where clauses preserve the shape of the original array
adults = np.where(ages>18, ages,0)
print(adults)