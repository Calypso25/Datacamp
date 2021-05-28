"""
You will now use your ecdf() function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF.
"""
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers,y_vers,marker = '.', linestyle ='none' )

# Label the axes
_ = plt.ylabel("ECDF")
_ = plt.xlabel("Petal length")

# Display the plot

plt.show()