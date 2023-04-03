# Defines the call ipClass
def ipClass(ip):
  
  octet = ip.split(".")
  
  # If octet is between 0 and 127 the ip is class A
  if(int(octet[0]) >= 0 and int(octet[0]) <= 127):
    
    return "\nClass: A"
  
  # If octet is between 128 and 191 the ip is class B
  elif(int(octet[0]) >=128 and int(octet[0]) <= 191):
    
    return "\nClass: B"
  
  # If octet is between 192 and 223 the ip is class C
  elif(int(octet[0]) >= 192 and int(octet[0]) <= 223):
    
    return "\nClass: C"
  
  # If octet is between 224 and 239 the ip is class D
  elif(int(octet[0]) >= 224 and int(octet[0])<= 239):
    
    return "\nClass: D"
  
  # If octet is between 240 and 255 the ip is class E
  elif(int(octet[0]) >= 240 and int(octet[0]) <= 255):
    
    return "\nClass: E"
  
  # If octet is anything else and error will be printed
  else:
    
    return "\nError Invalid IP"

# Defines the class main
def main():
  
  ip = input("Please enter a valid IP address : ")
  print("IP Address:", ip, ipClass(ip))
  
main()