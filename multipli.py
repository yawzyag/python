import numpy as np

# delacaracion de las 2 array
A = ([1, 6, 5], [3, 4, 8], [2, 12, 3])
B = ([3, 4, 6], [5, 6, 7], [6, 56, 7])

# uso de numpy para multiplicar las 2 array
C = np.dot(A, B)

print(C)
