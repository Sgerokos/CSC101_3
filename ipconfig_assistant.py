# Imports the required modules
import subprocess
import sys

# Requests the user to select one of the following
ip = input("Please Enter One of The Following: " 
             "\n1 for ipconfig," 
             "\n2 for ipconfig /all,"
             "\n3 for ipconfig /renew," 
             "\n4 for ipconfig /renew EL*," 
             "\n5 for ipconfig /release *Con*,"
             "\n6 for ipconfig /allcompartments," 
             "\n7 foripconfig /allcompartments /all," 
             "\nor help for Assistance in Choosing: " )

# If help is entered list's the algorithms and what they are
if ip == ("help"):
    
    print("\n1 ipconfig will show information on ip configuration"
          "\n2 ipconfig /all will show detailed" 
          "information on ip configuration"
          "\n3 ipconfig /renew will renew all adapters,"
          "\n4 ipconfig /renew EL* will renew any connection" 
          "that has its name starting with EL"
          "\n5 ipconfig /release *Con* release all matching connections,"
          "\nFor Example: Wired Ethernet Connection 1 or"
          "Wired Ethernet Connection 2," 
          "\n6 ipconfig /allcompartments will show" 
          "information about all compartments,"  
          "\n7 ipconfig /allcompartments /all will how detailed" 
          "information about all compartments\n")
    
    # Re ask's the user to select one of the following
    ip = input("Please Re Enter One of The Following." 
               "\n1 for ipconfig," 
               "\n2 for ipconfig /all,"
               "\n3 for ipconfig /renew," 
               "\n4 for ipconfig /renew EL*," 
               "\n5 for ipconfig /release *Con*,"
               "\n6 for ipconfig /allcompartments," 
               "\n7 foripconfig /allcompartments /all," 
               "\nor help for Assistance in Choosing:" )
    
# If 1 is selected the system
# will show information 
# on the ip configuration     
if ip == ("1"):
        
    subprocess.call("ipconfig",shell=True)
    
# If 2 is selected the system
# will show detailed information 
# on the ip configuration 
elif ip == ("2"):
            
    subprocess.call("ipconfig /all",shell=True)

# If 3 is selected the system will 
# will renew all adapters  
elif ip == ("3"):
            
    subprocess.call("ipconfig /renew",shell=True)
    
# If 4 is selected the system will 
# will renew any connection
# that has its name starting with EL  
elif ip == ("4"):
                
    subprocess.call("ipconfig /renew EL*",shell=True)
    
# If 5 is selected the system will 
# release all matching connections       
elif ip == ("5"):
                    
    subprocess.call("ipconfig /release *Con*",shell=True)

# If 6 is selected the system will 
# print out all information on compartments
elif ip == ("6"):
                
    subprocess.call("ipconfig /allcompartments",shell=True)
    
# If 7 is selected the system will 
# print out all the detailed information
# about all compartments
elif ip == ("7"):
                    
    subprocess.call("ipconfig /allcompartments /all",shell=True)    

# If anything else is entered the system will exit 
# with an error Message 
else:
    print("\n\nSorry Wrong Input." 
        "\nPlease Try Again." 
        "\nNow Exeting!!!")
    sys.exit()