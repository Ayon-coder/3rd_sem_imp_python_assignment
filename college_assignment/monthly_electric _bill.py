import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"],
    "Bill": np.random.randint(500, 3000, 12)
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(1, 3, figsize=(20,6))

# Line plot
ax[0].plot(df["Month"], df["Bill"])
ax[0].set_title("Line Plot")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Bill")

# Pie chart
ax[1].pie(df["Bill"], labels=df["Month"], autopct="%1.1f%%")
ax[1].set_title("Pie Chart")

# Horizontal bar chart
ax[2].barh(df["Month"], df["Bill"])
ax[2].set_title("Barh Chart")
ax[2].set_xlabel("Bill")
ax[2].set_ylabel("Month")

plt.tight_layout()
plt.show()