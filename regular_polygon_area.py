# Imports modules
import math, sys

def area(n, s):
    # Evaluates the area of a regular polygon
    a = (n * s ** 2) / (4 * math.tan(math.pi / n))
    
    # Print's the area of the polygon for the user
    print("The Area of The Polygon is", a)    
    
# Read's the input from the user
n = float(input("Please Enter The Number of Sides: "))
# If n equal 0 or less than 0 system exit
if n < 0:
    print("Inpropper input. Only Positive number's" 
        "\nGreater Than 1 Are Accepted")
    sys.exit()  
# Read's the input from the user
s = float(input("Please Enter The Side: "))
# If s equal 0 or less than 0 system exit
if s < 0:
    print("Inpropper input. Only Positive number's" 
        "\nGreater Than 1 Are Accepted")
    sys.exit() 

area(n,s)