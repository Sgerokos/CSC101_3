# Imports the sys package into python
import sys

def subTotal(price):
    
    # This variable is the tax 8.75%
    sales_Tax = 0.0875
    
    # Variable's used
    # Tax will be calculated by price times sales_Tax
    tax = menu.price * sales_Tax
    
    # Total will add price and tax
    total = menu.price + tax
    
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
    print("Order's:", menu.order, "\nSide's:", side.sides, 
          "\nTotal Without Tax", price,
          "\nThe Total With Tax is:", round(total, 2),
          "\nThe Total is:", round(total, 2), 
          "\nThe Sale's Tax is:", round(tax, 2), 
          "\n10% Tip is:", round(ten_Tip, 2), 
          "15% Tip is:", round(fifteen_Tip, 2), 
          "20% Tip is:", round(twenty_Tip, 2),
          "25% Tip is:", round(twenty_Five_tip, 2),
          "30% Tip is:", round(thirty_Tip, 2))
    sys.exit()    

def side():
    
    side.sides = ""
    
    # Ask's for a choice in side       
    s = input("Do You Want Chicken Orzo Soup or" 
                  "\nOrganic Field Greens as a Side"
                  "\nPlease Select 1 For Chicken Orzo Soup"
                  "\nor 2 For Field Greens: ")  
    if s == 1:
        yn = input("Do You Want to Add Chicken Orzo Soup as the Side? "
                     "\nY For Yes N For No: ")
        
        # If Y is selected the side will be added
        if yn == "Y":
            side.sides += "Chicken Orzo Soup"

        # If N is selected the side will not be added
        elif yn == "N":
            side.sides += ""   
            
            
    # Choice two for side           
    if s == 2:
        y_N = input("Do You Want to Add Chicken Field Greens as the Side? "
                     "\nY For Yes N For No: ")
        
        # If Y is selected the side will be added
        if y_N == "Y":
            side.sides += "\nField Greens"
             
        # If N is selected the side will not be added
        elif y_N == "N":
            side.sides += "" 
            

def yesNo():  
    # This variable will change line 15 look at line 14
    something_Else = input("Would You Like Something Else? \
                          \nPlease Enter Y For Yes or N For No:")
    if something_Else == "Y":
        userInput()
    
    # If N is selected the folowing will be used        
    elif something_Else == "N":    
        
        subTotal(menu.price)
        
    # If a anything besides Y or N is selected an error message will be printed  
    elif something_Else != "N" or something_Else != "Y":
        return "Bad Input", userInput()
    
def userInput():
    # Welcome's the user to the establiment
    print("Hello Welcome to Sanfords Restaurant"
          "\nWhat Can I Serve You Today?")
    
    # Ask's the user to input a number for one of the items
    e = int(input("Please Select One of The Following Entrées:"
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
    return e
        
def menu(entrees):
    
    # The price is 0 but will be changed as the loop continue's or end's
    menu.price = 0    
    
    # variable order will be set as an empty string till all selections are made
    menu.order = ""
    
    while entrees != 0:
        
        # If a number not used is selected an error message will be printed out 
        if entrees < 1 or entrees > 10:
    
            print("\nYou have Inputed an Invalid Number For The Entrées"
                  "\nPlease Enter a number Between 1 - 10 For This Selection")
            
        # Line's 33 - 108 are the selection's that the user will choose from
        # The choice selected will print out what the item is and the price
        elif entrees == 1:
            print("Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs," 
                  "\ncilantro cream sauce." 
                  "\nPrice: $26")
                    
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 26
                menu.order += "\nLinguini With Stuffed Meatballs: $26"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
    
        elif entrees == 2:     
            print("Vegetable Paella  - Roasted seasonal vegetables, mushrooms,"
                  "\nsweet potato, organic red quinoa," 
                  "\nPrice: $24") 
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 24
                menu.order += "\nVegetable Paella: $24"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                               
        elif entrees == 3:
            print("Braised Short Rib Cavatelli - Baked with mushrooms," 
                  "\npearl onions, whipped ricotta" 
                  "\nPrice: $29")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 29
                menu.order += "\nBraised Short Rib Cavatelli: $29"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                                 
        elif entrees == 4:    
            print("Irish Organic Salmon - Flemon cous cous, rustic garden vegetables," 
                  "\ntomatoes, capers, white wine sauce." 
                  "\nPrice: $29")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 29
                menu.order += "\nIrish Organic Salmon: $29"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                                      
        elif entrees == 5:
            print("Teriyaki Chicken - Organic chicken, jasmine rice,"
                  "\navocado, stir-fried vegetables" 
                  "\nPrice: $26")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 26
                menu.order += "\nTeriyaki Chicken: $26"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                            
        elif entrees == 6:
            print("Rigatoni With Chicken - Organic chicken," 
                "\nhouse oven dried tomato cream sauce"
                "\nPrice: $26")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 26
                menu.order += "\nRigatoni With Chicken: $26"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                
        elif entrees == 7:
            print("Lobster Ravioli  - North atlantic lobster, sherry cream sauce" 
                  "\nPrice: $32")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 32
                menu.order += "\nLobster Ravioli: $32"
            
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                           
        elif entrees == 8:
            print("Seafood Risotto - Shrimp, calamari, shellfish broth," 
                  "\nvegetable mire poix."
                  "\nPrice: $30")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 30
                menu.order += "\nSeafood Risotto: $30"
            
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                
        elif entrees == 9:
            print("Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts," 
                  "\nenoki mushrooms, peppers, carrots, soy-ginger broth" 
                  "\nPrice: $30")        
                
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 30
                menu.order += "\nSesame Crusted Yellowfin Tuna: $30"
                
                side()
                    
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                
    
        elif entrees == 10:
            print("Blackened Prime Ribeye Steak - Cast iron seared," 
                  "\n20oz bone in prime ribeye." 
                  "\nSweet potato au gratin." 
                  "\nPrice: $52")
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                menu.price += 52
                menu.order += "\nBlackened Prime Ribeye Steak: $52"
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                menu.order += ""
                
        
        yesNo()
        
    return price, order

            

        
def main():
    
    entrees = userInput()
    menu(entrees)
    yesNo()
    side()
    subTotal()
    
main()