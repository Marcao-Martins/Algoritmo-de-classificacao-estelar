import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 3, 7, 6, 8, 9, 10, 11, 13]
classes = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
plt.scatter(x,y, c=classes)
print("CU\n")
plt.show()
