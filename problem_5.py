import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Generate corresponding x values (indices)
x = np.arange(len(data))

# Plot scatter graph
plt.figure(figsize=(10, 6))
plt.scatter(x, data, color='blue', alpha=0.5, s=10)

# Add labels and title
plt.title('Scatter Plot of 1000 Random Numbers from Normal Distribution')
plt.xlabel('Index') 
plt.ylabel('Value')
plt.grid(True)

# Show plot
plt.show()
