# Imports math module
import math

# Read's the input from the user
n = float(input("Please Enter The Number of Sides:"))
s = float(input("Please Enter The Side:"))

# Evaluates the area of a regular polygon
a = (n * s ** 2) / (4 * math.tan(math.pi / n))

# Print's the area of the polygon for the user
print("The Area of The Polygon is", a)