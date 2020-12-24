# sorting array using np.sort()
# import numpy as np
# arr = np.array([3,2,0,1])
# print(np.sort(arr))


# sorting alaphetical array using np.sort()
# import numpy as np
# arr = np.array(['banana','apple','cherry'])
# print(np.sort(arr))

# sorting boolean array using np.sort()
# import numpy as np
# arr = np.array([True, False, True])
# print(np.sort(arr))

# sorting a 2-D array using np.sort()
# import numpy as np
# arr = np.array([[3,2,0,1],[5,1,2,9]])
# print(np.sort(arr))

# simple filtering 
# import numpy as np
# arr = np.array([41,42,43,44])
# x = [True,False,True,False]
# newarr = arr[x]
# print(newarr)

# creating filter array with numbers higher than 42  
# import numpy as np
# arr = np.array([41,42,43,44])

# filter_arr = []

# for element in arr:
# 	if element > 42:
# 		filter_arr.append(True)
# 	else:
# 		filter_arr.append(False)

# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

# x = [True,False,True,False]
# newarr = arr[x]
# print(newarr)
import numpy as np
arr = np.array([41,42,43,44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)






