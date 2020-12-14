# how to create basic numpy array
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# to see the version of numpy
# print(np.__version__)

# to see the type of numpy array
# print(type(arr))


# O-D Arrays
# import numpy as np
# arr = np.array(42)
# print(arr)

# 1-D Arrays
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# 2-D Arrays
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

# 3-D Arrays
# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr)

# print(arr.ndim)

# Higher level dimensions
import numpy as np
arr = np.array([1,2,3,4,5], ndmin = 5)
print(arr.ndim)
print(arr)

