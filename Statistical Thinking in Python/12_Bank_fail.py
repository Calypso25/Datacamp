"""
Plot the number of defaults you got from the previous exercise, in your namespace as n_defaults, as a CDF. 
If interest rates are such that the bank will lose money if 10 or more of its loans are defaulted upon, 
what is the probability that the bank will lose money?
"""
# Compute ECDF: x, y
x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.ylabel("ECDF")
_ = plt.xlabel("Number of defaults")
_ = plt.plot(x,y, marker = '.', linestyle ='none' )

# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))