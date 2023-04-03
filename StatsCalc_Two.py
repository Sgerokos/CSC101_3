# Import math module
import math

# Defines the deviation function
def deviation(user_Input):

    # Call's the mean function
    mean(user_Input)

    # Get's the standad deviation
    var = math.sqrt((1/len(user_Input)) * sum((i - mean(user_Input)) ** 2 for i in user_Input))

    return var

# Defines the mean function
def mean(user_Input):

    # Get's the average from the input's
    mean = sum(user_Input) / len(user_Input)

    return mean 

# Defines the main method
def main():

    # Ask's for user input
    user_Input = list(map(float,input("Please Enter Ten Digit's Seperated by Commas" 
                                "\nEx: 1, 2, 3, 4, 5, etc:  \n").split(", ")))
    # Call's the deviation function
    deviation(user_Input)
    
    # Print's output
    print("\nThe Mean is:\n" + str(round(mean(user_Input), 2)), 
          "\n\nThe Standart Deviation is:\n"
          + str(round(deviation(user_Input), 5)))
   

# Call's the main function
main()