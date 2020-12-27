# add two arrays using numpy ufunc add method
# import numpy as np
# x = [1,2,3,4]
# y = [5,6,7,8]
# z = np.add(x, y)
# print(z)

# create your own ufunc addition method
# import numpy as np

# def myadd(x,y):
# 	return x+y

# myadd = np.frompyfunc(myadd, 2, 1)
# print(myadd([1,2,3,4],[5,6,7,8]))

# check the type of function
# import numpy as np
# print(type(np.concatenate))

# check in if statement if the function is a unfuc function
import numpy as np

if type(np.add) == np.ufunc:
	print('add is ufunc')
else:
	print('add is not ufunc')
