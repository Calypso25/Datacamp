"""
Plot a histogram of the petal lengths of his 50 samples of Iris versicolor 
using matplotlib/seaborn's default settings
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
plt.hist(versicolor_petal_length)

# Show histogram
plt.show()