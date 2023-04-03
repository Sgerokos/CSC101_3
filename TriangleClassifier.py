import sys

# requests the user to input the three sides of the triangle
a = int(input("Welcome to Triangle Type!!!"
               "\nPlease Enter The Length of The First Side: "))
b = int(input("\nPlease Enter The Length of The Second Side: "))
c = int(input("\nPlease Enter The Length of The Third Side: "))

if a < 0 or b < 0 or c < 0:
    print("\nInproper Input Sides Must Be Greater Than 0")
    sys.exit()
    
# If the three sides are equal to eachother 
# the program will print this line out 
if a == b == c:

    print("\nThis is a Equilateral Triangle")

# If the three sides are not equal to eachother 
# the program will print this line out 
elif a != b != c:

    print("\nThis is a Scalene Triangle")
    
# If the three sides congruent with eachother
# the program will print this line out 
elif a == b:

    print("\nThis is a Isosceles Triangle")

elif b == c:
    
    print("\nThis is a Isosceles Triangle")
    
elif c == a:
    
    print("\nThis is a Isosceles Triangle")