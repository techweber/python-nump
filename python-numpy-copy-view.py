# example of array copy
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

# examply of array view
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[1] = 150
# print(arr)
# print(x)

# examply of array base to check if array owns its data
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
print (x.base)
print (y.base)