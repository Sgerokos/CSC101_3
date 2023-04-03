# Read's user inputs
v0 = float(input("Please Enter Starting Velocity(m/s), Vo: "))
v1 = float(input("Please Enter Final Velocity(m/s), V1: "))
t = float(input("Please Enter Time Span (seconds), t: "))

# Evaluates average acceleration using the formula
a = (v1 - v0) / t

# Print's average acceloration for the user
print(a)