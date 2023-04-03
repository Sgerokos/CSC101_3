# Variables that will take in the required input from the user
w1 = float(input("What is The Weight For Package 1: "))
p1 = float(input("Please Enter Price For Package 1: "))
w2 = float(input("What is The Weight For Package 2: "))
p2 = float(input("Please Enter Price And Price For Package 2: "))


package_1 = p1 / w1
package_2 = p2 / w2

# If statement if w1 and p1 are less than w2 and p2 
# the first print statement will print 
# if anything else the second will print
if package_1 < package_2:
    
    print("Package 1 Has A Better Price.")
    
elif package_2 < package_1:
        
    print("Package 2 Has A Better Price.")
    
elif package_1 == package_2:
        
    print("Both Packages Are Equal.")
    
else:
    
    print("Invalide Input")