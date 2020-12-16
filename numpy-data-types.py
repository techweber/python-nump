# import numpy as np

# arr = np.array(['a','b','c'], dtype="i")

# print(arr)
# print(arr.dtype)

import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)