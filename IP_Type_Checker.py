# Defines the function IPv4
def IPv4(ipv4):
  
  # For loop to check the range of each number between the periods
  for x in ipv4:
    
    # If ipv4 is between 0 and 255 or ipv[] does not equal 0 and equals 1 valid
    if((int(x) >= 0 and int(x) <= 255) or (x[0] != "0" and len(x) == 1)):

      return ".".join(ipv4), "is a Valid IPv4 IP Address", 

    # Else invalid
    else:

      return ".".join(ipv4), "is an Invalid IPv4 IP Address"

# Defines the function IPv6
def IPv6(ipv6):

  # For loop
  for i in ipv6:

    # If len(i) is less than or equal to 4 continue
    if (len(i) <= 4):

      # For loop length of grooup can be 1-4
      for x in range(len(i)):

         # The ord() function will return the ASCII value
         # ASCII value of 0-9 is 48-57, A-F is 65-70, and a-f is 97-102
         # If great or equal to 48 and less than or equal to 57
         # Or greater or equal to 65 and less than or equal to 70
         # Or greater or equal to 97 and less than or equal to 102
         # Will return valid 
          if ((ord(i[x]) >= 48 and ord(i[x]) <= 57) 
              or (ord(i[x]) >= 65 and ord(i[x]) <= 70) 
              or (ord(i[x]) >= 97 and ord(i[x]) <= 102)):

            return ":".join(ipv6), "is a Valid IPv6 IP Address"

      # Else invalid
      else:

        return ":".join(ipv6), "is an Invalid IPv6 IP Address"

# Defines the function ipType
def ipType(ip):
  
  # variables ipv4 and ipv6 will split the input
  # ipv4 will split the . from the input
  # ipv6 will split the : from the input
  ipv4 = ip.split(".")
  ipv6 = ip.split(":")
  
  # If input count is 4 or 8
  if len(ipv4) == 4 or len(ipv6) == 8:
    
    # If input count is 4 return IPv4(ipv4)
    if len(ipv4) == 4:

      return IPv4(ipv4)
    
    # If input count is not 4 and is count 8 return IPv6(ipv6)
    elif len(ipv4) != 4 and len(ipv6) == 8:

      return IPv6(ipv6)
    
  # Else return error with input
  else:

      return ip, "is Neither IPv4 or IPv6"

# Defines the main function
def main():

  # Infinite while loop to ask the user for input and print
  while True:

    ip = input("\nPlease Enter a Valid IP Address : \n")
    print("\nIP Address:", *ipType(ip))

# Call's the main function
main()