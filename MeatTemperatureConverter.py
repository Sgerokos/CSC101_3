# Ask's the user to input 1 for Fahrenheit or 2 for celsius
option = int(input("Welcome to Beef, Veal, and Lamb"
                   "\nInternal Temperature Chart:"
                   "\nFahrenheit and Celsius Cooking Temperatures"
                   "\nPlease Select 1 For Fahrenheit or 2 For Celsius: "))

# Line's 15 - 80 are for option 1
# it will print the selection and ask the user to input the tempurature
# the program will also convert from fahrenheit to celsius
# the program will also print out how much higher the tempurture 
# is required to be to get the the higher doneness 
if option == 1:
    print("You Have Selected Fahrenheit")
    
    f = int(input("Please Enter The Internal Core Temperature" 
                     "\nFor Fahrenheit 120-164: "))
    
    # Calculates Celsius
    c = (f - 32) / 1.8
    
    # Starting temperature for for doneness
    rare = 120
    medium_Rare = 130
    medium = 140
    medium_Well = 150
    well_Done = 160
    
    # If f <= 120 and f < 125:
    if 120 <= f <= 125:   
        print("The Meat is Rare - Center is bright red," 
              "\npinkish toward the exterior portion,"
              "\nand warm throughout."
              "\nThe Tempurature Entered is", f, "Degrees Fahrenheit"
              "\nAnd", round(c), "Degrees Celsius"
              "\nCook for", medium_Rare - f, "more degrees for Medium Rare"
              "\nCook for", medium - f, "more degrees for Medium"
              "\nCook for", medium_Well - f, "more degrees for Medium Well"
              "\nCook for", well_Done - f, "more degrees for Well Done")
        
    # If f <= 130 and f <= 135:
    elif 130 <= f <= 135:   
        print("The Meat is Medium Rare - Center is very pink," 
              "\nslightly brown toward the exterior portion,"
              "\nand slightly hot."
              "\nThe Tempurature Entered is", f, "Degrees Fahrenheit"
              "\nAnd", round(c), "Degrees Celsius"
              "\nCook for", medium - f, "more degrees for Medium"
              "\nCook for", medium_Well - f, "more degrees for Medium Well"
              "\nCook for", well_Done - f, "more degrees for Well Done")   
                
    # If f <= 140 and f <= 145:
    elif 140 <= f <= 145:   
        print("The Meat is Medium - Center is light pink," 
              "\nouter portion is brown, and hot throughout"
              "\nThe Tempurature Entered is", f, "Degrees Fahrenheit"
              "\nAnd", round(c), "Degrees Celsius"
              "\nCook for", medium_Well - f, "more degrees for Medium Well"
              "\nCook for", well_Done - f, "more degrees for Well Done")   
    
    # If f <= 150 and f <= 155:
    elif 150 <= f <= 155:   
        print("The Meat is Medium Well - Mostly gray-brown throughout" 
              "\nwith a hint of pink in the center"
              "\nThe Tempurature Entered is", f, "Degrees Fahrenheit"
              "\nAnd", round(c), "Degrees Celsius"
              "\nCook for", well_Done - f, "more degrees for Well Done")
    
    # If f <= 155 and f <= 164:
    elif 155 <= f <= 164:   
        print("The Meat is Medium Well - Mostly gray-brown throughout" 
              "\nwith a hint of pink in the center"
              "\nThe Tempurature Entered is", f, "Degrees Fahrenheit"
              "\nAnd", round(c), "Degrees Celsius")
    
    # If the input is anything besides what is allowed 
    # This error message will be printed        
    else:
        print("The Input You Have Entered is Not Recognized." 
              "\nPlease Input a Number Ranging From 120-164." 
              "\nThank You!!!")        

# Line's 87 - 162 are for option 2
# it will print the selection and ask the user to input the tempurature
# the program will also convert from celsius to fahrenheit
# the program will also print out how much higher the tempurture 
# is required to be to get the the higher doneness         
elif option == 2:
    print("You Have Selected Celsius")
    
    c = int(input("Please Enter The Internal Core Temperature" 
                     "\nFor Celsius 49-73: "))  
    
    # calculate fahrenheit
    f = (c * 1.8) + 32
    
    # Starting temperature for for doneness
    rare = 49
    medium_Rare = 55
    medium = 60
    medium_Well = 65
    well_Done = 70
    
    # If c <= 49 and c <= 51:
    if 49 <= c <= 51:   
        print("The Meat is Rare - Center is bright red," 
              "\npinkish toward the exterior portion,"
              "\nand warm throughout."
              "\nThe Tempurature Entered is", c, "Degrees Celsius"
              "\nAnd", round(f), "Degrees Fahrenheit"
              "\nCook for", medium_Rare - c, "more degrees for Medium Rare"
              "\nCook for", medium - c, "more degrees for Medium"
              "\nCook for", medium_Well - c, "more degrees for Medium Well"
              "\nCook for", well_Done - c, "more degrees for Well Done")
        
    # If c <= 55 and c <= 57:
    elif 55 <= c <= 57:   
        print("The Meat is Medium Rare - Center is very pink," 
              "\nslightly brown toward the exterior portion,"
              "\nand slightly hot."
              "\nThe Tempurature Entered is", c, "Degrees Celsius"
              "\nAnd", round(f), "Degrees Fahrenheit"
              "\nCook for", medium - c, "more degrees for Medium"
              "\nCook for", medium_Well - c, "more degrees for Medium Well"
              "\nCook for", well_Done - c, "more degrees for Well Done")   
                    
    # If f <= 60 and f <= 63:
    elif 60 <= c <= 63:   
        print("The Meat is Medium - Center is light pink," 
              "\nouter portion is brown, and hot throughout"
              "\nThe Tempurature Entered is", c, "Degrees Celsius"
              "\nAnd", round(f), "Degrees Fahrenheit"
              "\nCook for", medium_Well - c, "more degrees for Medium Well"
              "\nCook for", well_Done - c, "more degrees for Well Done")   
        
    # If c <= 65 and c <= 69:
    elif 65 <= c <= 69:   
        print("The Meat is Medium Well - Mostly gray-brown throughout" 
              "\nwith a hint of pink in the center"
              "\nThe Tempurature Entered is", c, "Degrees Celsius"
              "\nAnd", round(f), "Degrees Fahrenheit"
              "\nCook for", well_Done - c, "more degrees for Well Done")
        
    # If c <= 71 and c <= 73:
    elif 70 <= c <= 73:   
            print("The Meat is Medium Well - Mostly gray-brown throughout" 
                  "\nwith a hint of pink in the center"
                  "\nThe Tempurature Entered is", c, "Degrees Celsius"
                  "\nAnd", round(f), "Degrees Fahrenheit")
     
     # If the input is anything besides what is allowed 
     # This error message will be printed
    else:
        print("The Input You Have Entered is Not Recognized." 
              "\nPlease Input a Number Ranging From 49-73." 
              "\nThank You!!!")        
        
# If the input is anything besides what is allowed 
# This error message will be printed    
else:
    print("The Input You Have Entered is Not Recognized." 
          "\nPlease Input 1 For Fahrenheit or 2 For Celsius."
          "\nThank You!!!")