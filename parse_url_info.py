# Import's required libraries
from urllib.parse import urlparse, urlsplit

# Variable that stores the url
url = urlsplit("https://www.serebii.net/pokedex-swsh/")

# Print's the reqeuested information
print ("URL :", url.geturl(), 
       "\nScheme  :", url.scheme, 
       "\nNetloc  :", url.netloc, 
       "\nPath    :", url.path, 
       "\nHostname:", url.hostname, "(netloc in lower case)")

# This is a seprate program 
# you can keep the top or 
# bottom part to print the information
# Variable that stores the url
url = ("https://www.serebii.net/pokedex-swsh/")

# Print's the information by spliting the string
print("\n****************************************************************\n"
      "\nURL :", url,
      "\nScheme :", url[0 : 5],
      "\nNetloc :", url[8 : 23],
      "\nPath :", url[23 : 37])
