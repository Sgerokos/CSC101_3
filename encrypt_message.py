# Defines the function encryption
def encryption(s, cipher):
    
    return cipher.join(s)

# Defines the main function
def main():
    
    # Requests the users input and encrypts the input 
    # using the key thats inputed by the user as well 
    txt = input("Please Enter The Text You Want To Obfuscate: \n")
    key = input("\nPlease Input The Key You Want To Use To Obfuscate: \n")
    obfuscate = encryption(txt, key)
    print("\nThe Text Is: \n" + txt, 
          "\n\nThe Key Is: \n" + key, 
          "\n\nThe Obfuscated String Is: \n" + obfuscate)

# Call's the main function
main()