# generate a random integer between 1 and 100
# import numpy as np
# x = np.random.randint(100)
# print( x )

# generate a float between 0 and 1
# import numpy as np
# x = np.random.rand()
# print( x )

# generate a 1-d array with 5 random integers between 1 and 100
# import numpy as np
# x = np.random.randint(100, size=(5))
# print( x )

# return a value from array of give numbers
# import numpy as np
# x = np.random.choice([3,5,7,9], size=(5))
# print( x )

# data distribution
# import numpy as np
# x = np.random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(3,5))
# print( x )

# shuffling arrays
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# np.random.shuffle(arr)
# print( arr )

# using permutation
import numpy as np
arr = np.array([1,2,3,4,5])
print(np.random.permutation(arr))



