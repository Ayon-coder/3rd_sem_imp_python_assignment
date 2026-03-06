import numpy as np

a = np.random.randint(0, 10, (3, 3))

print(np.min(a, axis=0), "Column min")
print(np.max(a, axis=1), "Row max")