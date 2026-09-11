import numpy as np

squares = np.array(range(1, 100))**2
for i in squares:
    for j in squares:
        if (i % j == 0):
            print(i, "divides", j, "=", i/j)

