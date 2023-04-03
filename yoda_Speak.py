# Defines the function yoda_Speak
def yoda_Speak():

    # Concatenate the the lists
    yoda = words_Split.predicate + words_Split.subject + words_Split.verb

    # Joins the lists into a string
    yodish = " ".join(" ".join(x) for x in yoda) 

    return yodish

# Defines the function words_Split
def words_Split(user_Input):

    # Split's the user's input into a list
    items = user_Input.split()

    # Empty lists to be used for appending
    words_Split.subject = []
    words_Split.verb = []
    words_Split.predicate = []

    # Using list slicing to get the diffrent required parts 
    # and associate them to the proper variables
    subject, verb, predicate = items[:1], items[1:2], items[2:]

    # Append's the sliced parts to the proper lists
    words_Split.subject.append(subject)
    words_Split.verb.append(verb)
    words_Split.predicate.append(predicate)

def main():

    # Ask's for user input
    user_Input = input("Please Enter a Sentence" 
                       "\nThat You Would Like to Convert to Yodish: \n\n")
    words_Split(user_Input)
    print("\nYodish Form:")
    print()
    print(yoda_Speak())    

main()