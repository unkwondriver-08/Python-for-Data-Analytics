# v_stack = stack the other matrix below other - vertically 
# this is the same case as axis =0 
# h_stack = stack the other matrix side by side - horizontally 
# this is the same case as axis =1


import numpy as np

a = np.array([[1,2], 
              [3,4]])
b = np.array([[4,5],
              [6,7]])

print(np.vstack((a,b)))
print(np.hstack((a,b)))