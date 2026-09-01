# NaN is important because missing data is extremely common in analytics
# it can help us replace the missing values with nan\

import numpy as np
x = np.nan
print(x)

sales = np.array([100, 200, np.nan, 400, 500])
print(sales)

# check whether we have nan values in an array
print(np.isnan(sales)) #where ever we have true it is a nan value

# no of missing value
print(np.isnan(sales).sum())

# np nan sum
sales = np.array([100, 200, np.nan, 400])
print(np.sum(sales)) #this give sum as nan
# but if we want sum, apart from nan
print(np.nansum(sales))

#  simillary we can get min and max having nan
print(np.nanmin(sales))
print(np.nanmax(sales))
print(np.nanmean(sales))

# dont do np.nan == np.nan
# or sales == np.nan-- this gives error

# removing nan from array
sales = np.array([100, 200, np.nan, 400, np.nan])

clean_sales = sales[~np.isnan(sales)]

print(clean_sales)


# panda isna() different than than nan