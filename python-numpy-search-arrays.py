# where function using numpy arr, finding an element
# import numpy as np
# arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr==4)
# print(x)


# find indexes where values are even
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr%2==0)
# print(x)

# find indexes where values are odd
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr%2==1)
# print(x)

# using searchsorted() function with numpy
# import numpy as np
# arr = np.array([6,7,8,9])
# x = np.searchsorted(arr,7)
# print(x)

# using searchsorted() function with numpy, search from right side
# import numpy as np
# arr = np.array([6,7,8,9])
# x = np.searchsorted(arr,7,side='right')
# print(x)

# using searchsorted() function with multiple values
import numpy as np
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)




