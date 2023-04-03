# Defines the hashtag extractor function
def hastag_Extractor(user_Input):
    
    # Variable for hastags list
    hashtags = []
    
    # For loop to loop around the split input
    for x in user_Input.split():
    
        if x[0] == "#":
        
            hashtags.append(x)
                   
    return "Hashtags Found:", ' '.join(hashtags)

# Define's the mentions_extractor function
def mentions_Extractor(user_Input):

    # Variable for mentions list
    mentions = []

    # For loop to loop around the split input
    for x in user_Input.split():
        
        if x[0] == "@":
        
            mentions.append(x)
        
    return "Mentions Found:", ' '.join(mentions)

# Define's the main function  
def main():

    user_Input= "learn #cplusplus from @ATT and #java from @Oracle and #Python from @ThePSF"
    
    # Unhash this line and hash the previuse to change to input
    #user_Input = input("\nPlease Enter Twitter Post: ")
    print("")
    print(*hastag_Extractor(user_Input), "\n")
    print(*mentions_Extractor(user_Input))

# Call's the main function  
main()