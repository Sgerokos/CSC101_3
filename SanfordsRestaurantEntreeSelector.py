# Welcome's the user to the establiment
print("Hello Welcome to Sanfords Restaurant"
      "\nWhat Can I Serve You Today?")

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

# Line's 20 - 69 are the selection's that the user will choose from
# The choice selected will print out what the item is and the price
if entrees == 1:
    print("Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs," 
          "\ncilantro cream sauce." 
          "\nPrice: $26")
                                               
elif entrees == 2:     
    print("Vegetable Paella  - Roasted seasonal vegetables, mushrooms,"
          "\nsweet potato, organic red quinoa," 
          "\nPrice: $24") 
                                                     
elif entrees == 3:
    print("Braised Short Rib Cavatelli - Baked with mushrooms," 
          "\npearl onions, whipped ricotta" 
          "\nPrice: $29")
                                               
elif entrees == 4:    
    print("Irish Organic Salmon - Flemon cous cous, rustic garden vegetables," 
          "\ntomatoes, capers, white wine sauce." 
          "\nPrice: $29")
                                                    
                                                    
elif entrees == 5:
    print("Teriyaki Chicken - Organic chicken, jasmine rice,"
          "\navocado, stir-fried vegetables" 
          "\nPrice: $17.68")
            
elif entrees == 6:
    print("Rigatoni With Chicken - Organic chicken," 
        "\nhouse oven dried tomato cream sauce"
        "\nPrice: $26")            
                                               
elif entrees == 7:
    print("Lobster Ravioli  - North atlantic lobster, sherry cream sauce" 
          "\nPrice: $32")
                                               
elif entrees == 8:
    print("Seafood Risotto - Shrimp, calamari, shellfish broth," 
          "\nvegetable mire poix."
          "\nPrice: $30")
        
elif entrees == 9:
    print("Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts," 
          "\nenoki mushrooms, peppers, carrots, soy-ginger broth" 
          "\nPrice: $30")        
        
elif entrees == 10:
    print("Blackened Prime Ribeye Steak - Cast iron seared," 
          "\n20oz bone in prime ribeye." 
          "\nSweet potato au gratin." 
          "\nPrice: $52")

# If a number not used is selected an error message will be printed out 
# An else statement or elif statement can be used 
# Uncomment the statement underneath and comment the other to implament.

#elif entrees < 1 or entrees > 10:
else:
    print("You have Inputed an Invalid Number For The Entrées"
          "\nPlease Enter a number Between 1 - 10 For This Selection")
