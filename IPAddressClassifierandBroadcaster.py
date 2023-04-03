# initialize done variable with False value
done = False

# run loop until valid IP is entered
while(done == False) :
    # take user input
    ip = input("Please enter a valid IP address : ")
    # split the input by dot separator
    lst = ip.split(".")
    
    # check if length of splitted input is 4
    if len(lst) != 4:
        # if length is not 4, print error message and set done to False
        print ("You have not entered valid address.")
        done = False
    else:
        # if length is 4, set done to True and continue to next steps
        done = True

# check class of IP address
if int(lst[0]) <= 126 and int(lst[0]) >= 1:
    classIP = "A"
elif int(lst[0]) <= 191 and int(lst[0]) >= 128:
    classIP = "B"
elif int(lst[0]) <= 223 and int(lst[0]) >= 192:
    classIP = "C"
else:
    classIP = "other"

# check if IP address is a broadcast address
if classIP == "A" and int(lst[1]) == 255 and int(lst[2]) == 255 and int(lst[3]) == 255 :
    isBroadCast = True
elif classIP == "B" and int(lst[2]) == 255 and int(lst[3]) == 255 :
    isBroadCast = True
elif classIP == "C" and int(lst[3]) == 255 :
    isBroadCast = True
else :
    isBroadCast = False

# print the class and whether it is a broadcast address or not
if isBroadCast == True:
    print("IP address mentioned is of class ",classIP," and is a broadcast address")
else:
    print("IP address mentioned is of class ",classIP," and is not a broadcast address")
