import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dict = {
    'X': np.random.randint(0, 3000, 30),
    'Y': np.random.randint(0, 3000, 30)
}

df = pd.DataFrame(dict)

plt.title("X VS Y")
plt.scatter(df["X"], df["Y"])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()