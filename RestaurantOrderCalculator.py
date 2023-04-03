# Imports the sys package into python
import sys

# Welcome's the user to the establiment
print("Hello Welcome to Sanfords Restaurant"
      "\nWhat Can I Serve You Today?")

# This variable is the tax 8.75%
sales_Tax = 0.0875

# The price is 0 but will be changed as the loop continue's or end's
price = 0

# anything_Else will be set to Y till the user change's it in line 130
something_Else = "Y"

# As long as anything_Else is Y the loop will continue from here
while something_Else == "Y":
    
    # Ask's the user to input a number for one of the items
    entrees = int(input("Please Select One of The Following Entrées:"
                        "\n1 For Linguini With Stuffed Meatballs"
                        "\n2 For Vegetable Paella,"
                        "\n3 For Braised Short Rib Cavatelli,"
                        "\n4 For Irish Organic Salmon,"
                        "\n5 For Teriyaki Chicken,"
                        "\n6 For Rigatoni With Chicken,"
                        "\n7 For Lobster Ravioli,"
                        "\n8 For Seafood Risotto"
                        "\n9 For Sesame Crusted Yellowfin Tuna,"
                        "\n10 For Blackened Prime Ribeye Steak: "))

    # Line's 33 - 109 are the selection's that the user will choose from
    # The choice selected will print out what the item is and the price
    if entrees == 1:
        print("Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs," 
              "\ncilantro cream sauce." 
              "\nPrice: $26")
                
        price += 26
            
    elif entrees == 2:     
        print("Vegetable Paella  - Roasted seasonal vegetables, mushrooms,"
              "\nsweet potato, organic red quinoa," 
              "\nPrice: $24") 
        
        price += 24
                                                         
    elif entrees == 3:
        print("Braised Short Rib Cavatelli - Baked with mushrooms," 
              "\npearl onions, whipped ricotta" 
              "\nPrice: $29")
        
        price += 29
                                                   
    elif entrees == 4:    
        print("Irish Organic Salmon - Flemon cous cous, " 
              "\nrustic garden vegetables, tomatoes, capers, white wine sauce." 
              "\nPrice: $29")
        
        price += 29
                                                        
                                                        
    elif entrees == 5:
        print("Teriyaki Chicken - Organic chicken, jasmine rice,"
              "\navocado, stir-fried vegetables" 
              "\nPrice: $26")
        
        price += 26
                
    elif entrees == 6:
        print("Rigatoni With Chicken - Organic chicken," 
            "\nhouse oven dried tomato cream sauce"
            "\nPrice: $26")
        
        price += 26
                                                   
    elif entrees == 7:
        print("Lobster Ravioli  - North atlantic lobster, sherry cream sauce" 
              "\nPrice: $32")
        
        price += 32
                                                   
    elif entrees == 8:
        print("Seafood Risotto - Shrimp, calamari, shellfish broth," 
              "\nvegetable mire poix."
              "\nPrice: $30")
        
        price += 30
            
    elif entrees == 9:
        print("Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts," 
              "\nenoki mushrooms, peppers, carrots, soy-ginger broth" 
              "\nPrice: $30")        
            
        price += 30 
            
    elif entrees == 10:
        print("Blackened Prime Ribeye Steak - Cast iron seared," 
              "\n20oz bone in prime ribeye." 
              "\nSweet potato au gratin." 
              "\nPrice: $52")
        
        price += 52
                
    # This variable will change line 15 look at line 14
    something_Else = input("Would You Like Something Else?"
                           "\nPlease Enter Y For Yes or N For No:")
    
    # If N is selected the folowing will be used        
    if something_Else== "N":
            
            # Variable's used
            # Tax will be calculated by price times sales_Tax
            tax = price * sales_Tax
            
            # Total will add price and tax
            total = price + tax
            
            # This is 10% tip, total time's 10%
            ten_Tip = total * 0.10
            
            # This is 15% tip, total time's 15%
            fifteen_Tip = total * 0.15
            
            # This is 20% tip, total time's 20%
            twenty_Tip = total * 0.20
            
            # This is 25% tip, total time's 25%
            twenty_Five_tip = total * 0.25      
            
            # This is 25% tip, total time's 25%
            thirty_Tip = total * 0.30                  
            
            # This will print total along with the sale's tax  
            # As well as the recomended tip's and then exit
            print("The Total is:", round(total, 2), 
                  "\nThe Sale's Tax is:", round(tax, 2), 
                  "\n10% Tip is:", round(ten_Tip, 2), 
                  "15% Tip is:", round(fifteen_Tip, 2), 
                  "20% Tip is:", round(twenty_Tip, 2),
                  "25% Tip is:", round(twenty_Five_tip, 2),
                  "30% Tip is:", round(thirty_Tip, 2))
            sys.exit()
                  
    # If a anything besides Y or N is selected an error message will be printed        
    elif something_Else != "N" or something_Else != "Y":
        print("Bad Input", something_Else)

    # If a number not used is selected an error message will be printed out 
    # An else statement or elif statement can be used 
    # Uncomment the statement underneath and comment the other to implament.
    
    #elif entrees < 1 or entrees > 10:
    else:
        print("You have Inputed an Invalid Number For The Entrées"
              "\nPlease Enter a number Between 1 - 10 For This Selection")
