# Read's the user input
m = int(input("Please Enter The Number of Minutes:"))

# Evaluates the total number of days
t = (m / 60) / 24

# Evaluates the number of years and days
y = int(t / 365)
d = int(t % 365)

# Print's year's and day's for the user
print("Year's:", y, "Day's:", d)