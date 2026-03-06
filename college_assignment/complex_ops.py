import numpy as np

a = np.array(
    [
        [1 + 2j, 2 + 3j],
        [1 + 9j, 2 + 3j]
    ]
)

b = np.array(
    [
        [5 + 2j, 2 + 8j],
        [4 + 7j, 1 + 1j]
    ]
)

print("Addition is: \n", a + b)
print("Subtraction is: \n", a - b)
print("Multipliaction is: \n", a * b)
print("Division is: \n", a / b)