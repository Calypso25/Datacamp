"""
Box-and-whisker plot
"""
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set default Seaborn style
sns.set()

# Create bee swarm plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('Species')
_ = plt.ylabel('Petal length (cm)')

# Show the plot
plt.show()
