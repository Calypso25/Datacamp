'''
In this exercise, we'll generate lots of random numbers between zero and one, and then plot a histogram of the results. 
If the numbers are truly random, all bars in the histogram should be of (close to) equal height
'''
# Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# Set default Seaborn style
sns.set()

# Seed the random number generator
random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()