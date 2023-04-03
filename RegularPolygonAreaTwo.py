# Imports modules
import math
import sys

# Read's the input from the user
n = float(input("Please Enter The Number of Sides: "))


# If n is greater than 0
# it will go to the next if statement
if n > 0:
    
    # Read's the input from the user
    s = float(input("Please Enter The Side: "))
    
    # If s is greater than 0
    # it will evaluate the output
    if s > 0:
    
        # Evaluates the area of a regular polygon
        a = (n * s ** 2) / (4 * math.tan(math.pi / n))

        # Print's the area of the polygon for the user
        print("The Area of The Polygon is", a)
    
    # If n or s equal 0 or less than 0 system exit
    else:
        print("Inpropper input. Only Positive number's" 
              "\nGreater Than 1 Are Accepted")
        sys.exit()    
# If n or s equal 0 or less than 0 system exit
else:
    print("Inpropper input. Only Positive number's" 
        "\nGreater Than 1 Are Accepted")
    sys.exit()    
