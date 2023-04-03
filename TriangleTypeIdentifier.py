# Will ask the user to click yes "Y" to continue
triangle = input("Welcome to Triangle Type!!! \
                \nPlease Click Y to Continue: ")

while triangle == "Y":
    
    # requests the user to input the three sides of the triangle
    a, b, c = eval(input("\nPlease Enter The Length of The First Side, \
                         \b\nThe Length of The Second Side, \
                         \nAnd The Length of The Third Side \
                         \nPlease Enter Them In the Following Format a, b, c: "))
    
    if a + b >= c and b + c >= a and c + a >= b:
        
            # If the three sides are equal to eachother 
            # the program will print this line out 
            if a == b == c:
        
                print("\nThis is a Equilateral Triangle")
                
                # Will ask the user if they want to try new input's
                # If yes "Y" the program will start again if no 
                # "N" the program will end
                triangle = input("Would you Like to Input New Side's? \
                                 \nPlease Click Y For Yes N For No: ")   
                
            # If the three sides are not equal to eachother 
            # the program will print this line out 
            elif a != b != c:
        
                print("\nThis is a Scalene Triangle")
                
                # Will ask the user if they want to try new input's
                # If yes "Y" the program will start again if no 
                # "N" the program will end                
                triangle = input("Would you Like to Input New Side's? \
                                 \nPlease Click Y For Yes N For No: ")   
                
            # If the three sides congruent with eachother
            # the program will print this line out 
            elif a == b or b  == c or c == a:
            
                print("\nThis is a Isosceles Triangle")
                
                # Will ask the user if they want to try new input's
                # If yes "Y" the program will start again if no 
                # "N" the program will end                
                triangle = input("Would you Like to Input New Side's? \
                                 \nPlease Click Y For Yes N For No: ")
                
               
    else:
        
        # Will ask the user if they want to try new input's
        # If yes "Y" the program will start again if no 
        # "N" the program will end    
        triangle = input("\nThis is Not a Tringle Based Off of The Given Sides. \
                         \nWould you Like to Input New Side's? \
                         \nPlease Click Y For Yes N For No: ")