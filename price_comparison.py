# Variables that will take in the required input from the user
w1 = float(input("What is The Weight For Package 1: "))
p1 = float(input("Please Enter Price For Package 1: "))
w2 = float(input("What is The Weight For Package 2: "))
p2 = float(input("Please Enter Price And Price For Package 2: "))


# If statement if w1 and p1 are less than w2 and p2 
# the first print statement will print 
# if anything else the second will print
if ((p1 / w1) > (p2 / w2)):
    
    print("Package 2 Has A Better Price.")
    
else:
    
    print("Package 1 Has A Better Price.")