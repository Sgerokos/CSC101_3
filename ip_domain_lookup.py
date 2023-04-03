# Defines IP_addresses function with IP addresses list
def IP_addresses():
    
    IP_addresses.ip = ["74.125.236.145", "209.191.122.70", "207.46.232.182", 
          "74.125.236.151", "66.220.149.11", "74.125.236.142", "70.42.185.10", 
          "17.149.160.49", "67.228.110.120", "129.42.38.1", "216.239.116.157", 
          "64.34.119.12", "137.254.16.101", "138.197.63.241", "72.237.4.113", 
          "52.149.246.39", "157.240.229.174", "104.244.42.1", "69.172.200.183"] 

    return IP_addresses.ip

# Defines domain function with domain list
def domain():

    domain.domain = ["google.com", "yahoo.com", "microsoft.com", "gmail.com", 
              "facebook.com", "developer.android.com", "pcworld.com", 
              "apple.com", "wireshark.org", "ibm.com", "zdnet.com", 
              "stackoverflow.com", "oracle.com", "python.org", "utica.edu", 
              "duckduckgo.com", "instagram.com", "twitter.com", "pokemon.com"]  
    

    return domain.domain

# Defines search function which will search between the lists
# deepending on user input from menu function
def search(m):
    
    if m == 1:

        x = input("\nPlease Enter The Domain Name You Want to Add"
                  "\nExample: example.com: ")
        
        domain.domain.append(x)
        
        
        y = input("\nPlease EnterThe IP Address You Want to Add" 
                     "\nExample: 111.111.1.1: ")
        
        IP_addresses.ip.append(y)
        
        print(domain.domain, IP_addresses.ip)

    elif m == 2:

        i = input("Please Enter The Domain Name You Want to Search: ")
        
        if i in domain.domain:
            search = domain.domain.index(i)

            ip = IP_addresses.ip[search]
            
            print("The Domain Name is:", i, "The IP Address is:", ip)
        
        else:
            
            print("Error IP Not Found")
    
        
    elif m == 3:
        
        i = input("Please Enter The IP Adress You Want to Search: ")
        
        if i in IP_addresses.ip:
            
            search = IP_addresses.ip.index(i)
        
            d = domain.domain[search]
            
            print("The IP Address is:", i, "The Domain Name is:", d)
        
        else:
            
            print("Error IP Not Found")
    
    elif m == 0:
            
            print("You Have Selected:", m, "\nNow Exeting!!")

# Defines menu function
def menu():

    user_Input = int(input("Please Select One of The following From The Menu:"
                  "\n1: Add IP and Domain info"
                  "\n2: Look up IP address by domain name"
                  "\n3: Look up domain name by IP address"
                  "\n0: Quit \n"))

    return user_Input

# Defines main function
def main():
    IP_addresses()
    domain()
    
    m = menu()
    while m != 0:
        search(m)
        m = menu()
        
    
    
        

# Call's the main function
main()