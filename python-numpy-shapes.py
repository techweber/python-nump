# import numpy as np
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)

# import numpy as np
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print(arr.shape)

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)

import numpy as np
arr = np.array([[1,2,3,4],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)