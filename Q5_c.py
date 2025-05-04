# This code creates a 2x2 grid of subplots with different types of plots.
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(8, 6))

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

# Scatter plot
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Scatter Plot')

# Bar plot
axs[1, 0].bar([1, 2, 3], [3, 7, 5])
axs[1, 0].set_title('Bar Plot')

# Histogram
axs[1, 1].hist(np.random.randn(1000), bins=30)
axs[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()


