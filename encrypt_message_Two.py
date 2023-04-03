# Imports random module
import random

# Defines the function encryption
def encryption(txt, key):

        encrypted_Txt =""

        for c in txt:

                encrypted_Txt += c + obfuscate(key)

        return encrypted_Txt

# Defines the function obfuscate
def obfuscate(key):

        new_txt = ""
        
        for x in range(key):

                new_txt += chr(random.randint(33,127))

        return new_txt

# Defines the main function
def main():  

        # Requests the users input and encrypts the input
        # using the key thats inputed by the user as well
        txt = input("Please Enter The Text You Want To Obfuscate: \n")
        key = int(input("\nPlease Input The Key You Want To Use To Obfuscate: \n"))
        obfuscate(key)
        encryption(txt, key)
        print("\nThe Text Is: \n" + txt,
              "\n\nThe Key Is: \n", + key,
              "\n\nThe Obfuscated String Is:\n", encryption(txt, key))

# Call's the main function
main()