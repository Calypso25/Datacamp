"""
Plot a histogram of the petal lengths of his 50 samples of Iris versicolor 
using matplotlib/seaborn's default settings
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes
_ = plt.ylabel('count')
_ = plt.xlabel('petal length (cm)')

# Show histogram
plt.show()