#

import numpy as np

rng = np.random.default_rng()

rngs = np.random.default_rng(seed =1) #if we put this seed =1 then we will produce the same set of number again and again

print(rng.integers(1,7)) #generate any random number between 1 and 6 (7 is not inclusive)
print(rng.integers(low=1,high =8)) # this low and high tells the boundary between which i need numbers
print(rng.integers(low=1,high =8, size =4)) #the size tells the no of numbers generated
print(rng.integers(low=1,high =8, size =(4,3))) # generate it have with 4 rows and 3 columns of random numbers


# We can generate random numbers with help of  np.random.seed(seed=1)

import random

# Initialize with seed 42
random.seed(42) #this allow to genereate the same no again and again
print(random.randint(1, 100))  # Output: 82
print(random.randint(1, 100))  # Output: 15

# Reset to the same seed
random.seed(42)
print(random.randint(1, 100))  # Output: 82 (Exactly the same!)
print(random.randint(1, 100))  # Output: 15 (Exactly the same!)

# import numpy as np
# np.random.seed(seed=1)

# print(np.random.uniform(low=-1, high =1, size=3)) #uniform means uniform distribution, each value have qual chance of selection
# print(np.random.uniform(low=-1, high =1, size=(3,2)))