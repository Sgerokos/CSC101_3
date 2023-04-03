# Imports the sys package into python
import sys

def subTotal():
    
    # This variable is the tax 8.75%
    sales_Tax = [0.0875]
    
    
    # Variable's used
    # Tax will be calculated by price times sales_Tax
    # Total of the sides times the quantity
    total_Sides = [main.sides_Price[i] * main.ordered_Quantity[i] 
                   for i in range(len(main.sides_Price))]
    
    # Total of main dish times the quantity
    total_Main = [main.price[i] * main.ordered_Quantity[i] 
                  for i in range(len(main.price))]
    
    # Total of main dish and sides
    total = [total_Main[0] + total_Sides[0]]
    
    # Tip in list format
    tip = [0.10, 0.15, 0.20, 0.25, 0.30]
    
    # Tax will be multiplied by the total and rounded to the tenth
    tax = [round(total[0] * sales_Tax[0], 2)]
    
    # Total with no tax
    total_No_Tax = [round(sum(total))]

    # Total will add price and tax
    total_With_Tax = [round(sum(total + tax), 2)]

    # This is 10% tip, total time's 10%
    ten_Tip = [round(total_With_Tax[0] * tip[0], 2)]

    # This is 15% tip, total time's 15%
    fifteen_Tip = [round(total_With_Tax[0] * tip[1], 2)]

    # This is 20% tip, total time's 20%
    twenty_Tip = [round(total_With_Tax[0] * tip[2], 2)]

    # This is 25% tip, total time's 25%
    twenty_Five_tip = [round(total_With_Tax[0] * tip[3], 2)]      

    # This is 25% tip, total time's 30%
    thirty_Tip = [round(total_With_Tax[0] * tip[4], 2)]                 
    
    # This will print  the entire order 
    # with the total along with the sale's tax  
    # As well as the recomended tip's and then exit    
    for col_a, col_b, col_c, col_d, col_e in \
        zip(main.order, main.price, main.ordered_Quantity,
            main.sides, main.sides_Price):
        print("Order: %s Main Dish Price: $%0.2f " 
              "Quantity: %d Side: %s Side Order Price: $%0.2f"  
              %(col_a, col_b, col_c, col_d, col_e))
    for col_a, col_b, col_c, col_d in \
        zip(total_No_Tax, total_With_Tax, total_No_Tax, tax):
        print("Total Without Tax: $%0.2f Total With Tax: $%0.2f "
        "The Total is: $%0.2f Sale's Tax is: $%0.2f" 
              %(col_a, col_b, col_c, col_d))
    for col_a, col_b, col_c, col_d, col_e in \
        zip(ten_Tip, fifteen_Tip, twenty_Tip, twenty_Five_tip, thirty_Tip):
        print("Percent Tip is: $%0.2f 15 Percent Tip is: $%0.2f 20 Percent "
        "Tip is: $%0.2f 25 Percent Tip is: $%0.2f 30 Percent Tip is: $%0.2f" 
              %(col_a, col_b, col_c, col_d, col_e))

    sys.exit()

def side():
    
    # Variables containing lists of sides, 
    # side number's, and prices
    sides = []
    side_Items = []
    sides_Price =[]
    
    # Load's the side.txt data and reads the lines as a list
    side_file = open('sides.txt', 'r').readlines()
    
    # For loop to read line's
    for side_info in side_file:
        
        # Splits the sides into a list seperated by '
        side_info_as_list = side_info.split("'")
        
        # Variables to contain each item
        side_number = int(side_info_as_list[0])
        side_order = side_info_as_list[1].strip()
        side_price = int(side_info_as_list[2])
        
        # Append's items to the corrisponding lists
        side_Items.append(side_number)
        sides.append(side_order)
        sides_Price.append(side_price)
    
    # Print's the lists
    for col_a, col_b, col_c in zip(side_Items, sides, sides_Price):
        print("%d For: %s Price: $%d"  %(col_a, col_b, col_c))
        
    # Ask's for a choice in side       
    s = int(input("\nWhat Would You Want as a Side: "))    
    
    # Searches for the index based on the input
    x = side_Items.index(s)
    
    # Searches for the index in the list
    y = sides[x]
    z = sides_Price[x]
    
    # Appends the items found to the corisponding list
    main.sides.append(y)
    main.sides_Price.append(z)
    
    return main.sides, main.sides_Price

def yesNo():
    
    # This variable will change line 15 look at line 14
    something_Else = input("\nWould You Like Something Else? \
                          \nPlease Enter Y For Yes or N For No: ")

    if something_Else == "Y":
        menu()

    # If N is selected the folowing will be used        
    elif something_Else == "N":
        subTotal()

    # If a anything besides Y or N is selected an error message will be printed  
    elif something_Else != "N" or something_Else != "Y":
        return "Bad Input", userInput()
    
def ordered_Quantity():
    
    amount = int(input("\nHow Many Order's Would You Enjoy: "))
    print("")

    main.ordered_Quantity.append(amount)

    return main.ordered_Quantity
         
def confirmation(x):

    # The user will be asked if they want to add this to the order
    y_N = input("\nDo You Want to Add This to Your order? "
                "\nY For Yes N For No: ")

    # If Y is selected the price will be added to the variable price
    # The order variable will be added to the variable order
    if y_N == "Y":

        i = menu.ordered_Items.index(menu.entrees)
        
        s = menu.menu_Prices[i]
        
        main.price.append(s)

        m = menu.menu_Items[i]

        main.order.append(m)
        
        ordered_Quantity()

        side()

        return main.order, main.price
    # If N is selected no price will be added to the price variable
    # order variable will remain as it did before
    elif y_N == "N":

        menu.order.append("")

        return main.order, main.price

def menu():
    
    # Variables containing lists for order's
    menu.menu_Items = []
    menu.menu_Prices = []
    menu.ordered_Items = []
    menu.ordered_Quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                             11, 12, 13, 14, 15, 16, 17, 18, 19]

    # Load's the Menu.txt data and reads the lines as a list
    menu_file = open('Menu.txt', 'r').readlines()

    # For loop to read line's
    for menu_info in menu_file:

        # Splits the menu into a list seperated by '
        menu_info_as_list = menu_info.split("'")

        # Variables to contain each item
        menu_number = int(menu_info_as_list[0])
        menu_order = menu_info_as_list[1].strip()
        menu_price = int(menu_info_as_list[2])

        # Append's items to the corrisponding lists
        menu.ordered_Items.append(menu_number)
        menu.menu_Items.append(menu_order)
        menu.menu_Prices.append(menu_price)

    # Print's the lists
    for col_a, col_b, col_c in \
        zip(menu.ordered_Items, menu.menu_Items, menu.menu_Prices):
        print("%d For: %s Price: $%d"  %(col_a, col_b, col_c))

    menu.entrees = userInput()

    if menu.entrees == 1:
        confirmation(menu.entrees)

    elif menu.entrees == 2:
        confirmation(menu.entrees)

    elif menu.entrees == 3:
        confirmation(menu.entrees)

    elif menu.entrees == 4:
        confirmation(menu.entrees)

    elif menu.entrees == 5:
        confirmation(menu.entrees)

    elif menu.entrees == 6:
        confirmation(menu.entrees)

    elif menu.entrees == 7:
        confirmation(menu.entrees) 

    elif menu.entrees == 8:
        confirmation(menu.entrees)

    elif menu.entrees == 9:
        confirmation(menu.entrees)

    elif menu.entrees == 10:
        confirmation(menu.entrees)
        
    elif menu.entrees == 11:
        confirmation(menu.entrees)

    elif menu.entrees == 12:
        confirmation(menu.entrees)

    elif menu.entrees == 13:
        confirmation(menu.entrees)

    elif menu.entrees == 14:
        confirmation(menu.entrees)

    elif menu.entrees == 15:
        confirmation(menu.entrees)

    elif menu.entrees == 16:
        confirmation(menu.entrees)

    elif menu.entrees == 17:
        confirmation(menu.entrees) 

    elif menu.entrees == 18:
        confirmation(menu.entrees)

    elif menu.entrees == 19:
        confirmation(menu.entrees)

    elif menu.entrees == 20:
        confirmation(menu.entrees)    

    yesNo()

    return menu.entrees

# Defines the function userInput
def userInput():

    # Ask's the user to input a number for one of the items
    e = int(input("\nPlease Select One of The Following Entrées : "))

    return e

# Defines the main function
def main():
    
    # print's a welcome message for the user
    print("\nHello Welcome to Sanfords Restaurant"
          "\n\nWhat Can I Serve You Today?"
          "\n\nMenu:")
    
    # Variables containing lists from the selection's
    main.price = []
    main.order = []  
    main.sides = []
    main.sides_Price = []
    main.ordered_Quantity = []
    m = menu()

    while m != 0:

        m = menu()

main()