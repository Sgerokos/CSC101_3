#Function to Encrypt and Decrypt the String
def encrypt(s, cipher):
    return cipher.join(s)

def decrypt(s, cipher):
    return s.split(cipher)

#main program body
def main():
    #Encrypting Plain Text to Cipher Text
    txt = input("Please Enter The Text You Want To Obfuscate: \n")
    key = input("Please Input The Key You Want To Use To Obfuscate: \n")
    obfuscate = encrypt(txt, key)
    print("The encrypted string is :", obfuscate)
    
    #Decrypting Cipher Text to Plain Text
    pList = decrypt(obfuscate, key)
    
    #pList is in the form of a List, converting back it to string below
    txt =''.join(pList)
    print("The decrypted string is :", txt)
main()