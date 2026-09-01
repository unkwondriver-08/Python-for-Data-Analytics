# where is the numpy version of if else statements,
# so it checks if condition true, print this, else print this

import numpy as np
ages = np.array([15, 18, 21, 12, 30])


# do the same job using the loop
# result = []
# for age in ages:
#     if age >= 18:
#         result.append("Adult")
#     else:
#         result.append("Minor")
# print(result)

# # lets do the same job using the where

result= np.where(ages>= 18, "adult", "minor")
print(result)