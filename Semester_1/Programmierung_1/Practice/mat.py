import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 , 1000)

fig, ax = plt.subplots()
ax.plot(x, x, label="linear")
ax.plot(x, x**2, label="cubic")
ax.plot(x, x**0.5, label="root")
ax.set_xlabel("some label")
ax.set_ylabel("y value")
ax.set_title("Fancy Functions")
ax.legend()

plt.show()