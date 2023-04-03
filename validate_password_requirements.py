# Defines the function passwordCheck
def passwordCheck(password):

    # Check's to see if each fucnction is True
    # If all the function's are True 
    # the password is valid 
    # if any function is false the return statement 
    # or statements will be returned to the function
    if length(password) != True:

        return "Password is Less Than 8 Character's"

    elif digitcnt(password) != True:

        return "Password Requires One Or More Digit's"

    elif uppercase(password) != True:

        return "Password Requires One or More Uppercase Letter's"

    elif lowercase(password) != True:

        return "Password Requires One or More Lowercase Letter's"

    elif symbole(password) != True:

        return "Password Requires One or More Special Symboles"

    else:

        return "The Password is Valid"
        

# Defines the function length
def length(password):

    # Check's if the password is at least 8 charatcters or more
    if len(password) < 8:

        return False

    else:

        return True

# Defines the function digicnt
def digitcnt(password):

    digit_cnt = 0

    # Check's if the password contains digits
    for char in password:

            if char in "0123456789":

                digit_cnt += 1

    if digit_cnt < 1:

        return False

    else:

        return True

# Defines the function uppercase
def uppercase(password):

    uppercase_cnt = 0

    # Check's if the password contains an uppercase letter
    for char in password:

        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            uppercase_cnt += 1

    if uppercase_cnt < 1:

        return False

    else:

        return True

# Defines the function lowercase
def lowercase(password):

    lowercase_cnt = 0

    # Check's if the password contains a lowercase letter
    for char in password:

        if char in "abcdefghijklmnopqrstuvwxyz":

            lowercase_cnt += 1

    if lowercase_cnt < 1:

        return False

    else:

        return True

# Defines the function symbole
def symbole(password):

    symbole_cnt = 0

    # Check's if the password contains a special symbole
    for char in password:
        
        if char in "!@#$%^&*()+=":

            symbole_cnt += 1

    if symbole_cnt < 1:

        return False

    else:

        return True

# Defines the function main
def main():

    # Ask's for user input
    pw = input("\nPlease Enter The Password You Want To Validate" 
               "\nThe Passward Must Contain 8 Charcater's Minimum,"
               "\nAn Minimun of One Uppercase and One LowerCase letter,"
               "\nA Minimum of one Number,"
               "\nAnd One Special Symbole (!@#$%^&*()+=) : \n\n")

    # Print's output 
    print(passwordCheck(pw))

# Calls the main function
main()