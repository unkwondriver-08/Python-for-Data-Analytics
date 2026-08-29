#SHUFFLE THE ELEMENTS OF ARRAY

import numpy as np
rng = np.random.default_rng()
import random
array = np.array([1,2,3,4,5,6])
random.shuffle(array)
print(array)