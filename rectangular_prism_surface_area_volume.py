# Read's the input from the user
l = float(input("Please Enter The Rectangular Prism Length: "))
h = float(input("Please Enter The Rectangular Prism Height: "))
w = float(input("Please Enter The Rectangular Prism Width: "))
# Evaluates the surfice area of the rectangular prism 
sa = 2 * ((l * h) + (w * h) + (l * w))  
# Evaluates the volume of the rectangular prism 
v = l * h * w
# Print's the surfice area and the volume 
# of the of the rectangular prism for the user
print("Surfice Area is:", sa, "Volume is:", v)