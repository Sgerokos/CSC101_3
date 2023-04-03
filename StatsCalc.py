# Import math module
import math

# Defines the deviation function
def deviation(user_Input):

    mean = sum(user_Input) / len(user_Input)

    var = sum([((x - mean) ** 2) for x in user_Input]) / len(user_Input)

    res = var ** 0.5

    return res

# Defines the mean function
def mean(user_Input):

    n, mean = len(user_Input), 0.0 

    if n <= 1:

        return user_Input[0] 

    #For calculating average 
    for i in user_Input: 

        mean += float(i) 

    mean /= float(n) 

    return mean 

# Defines the main method
def main():
# Taking input

    user_Input = list(map(float,input("Please Enter Ten Digit's Seperated by Commas" 
                                "\nEx: 1, 2, 3, 4, 5, etc :  \n\n").split(", ")))
    deviation(user_Input)
    mean(user_Input)
    print("\nMean of the following is:\n", + round(mean(user_Input), 2))
    print("\nThe Standart deviation is:\n", + round(deviation(user_Input), 5))

# Call's the main function
main()