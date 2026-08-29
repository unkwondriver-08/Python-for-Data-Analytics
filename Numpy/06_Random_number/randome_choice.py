#SELECT A RANDOM ELEMENT CHOICE FROM AN ARRAY

import numpy as np
rng = np.random.default_rng()

# select one
fruits = np.array(["apple", "banana", "orange", "coconut"])
fruits= rng.choice(fruits)
print(fruits)


#select some size
fruits = np.array(["apple", "banana", "orange", "coconut"])
fruit= rng.choice(fruits, size =3)
print(fruit)
