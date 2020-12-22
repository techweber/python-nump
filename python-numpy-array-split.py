# splitting single dimension array into 3 arrays
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr)


# split array into 3 arrays and print contents of new array object
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# split 2-d array into 3 2-d arrays
# import numpy as np
# arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# newarr = np.array_split(arr,3)
# print(newarr)

# split array into arrays but using axis

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
# newarr = np.array_split(arr,3,axis=1)
newarr = np.hsplit(arr,3)
print(newarr)