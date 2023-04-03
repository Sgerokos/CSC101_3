# Read's the input from the user
amount = float(input("Please Enter The Amount You Would Want to Investment: "))
interest = float(input("Please Enter The Annual Interest Rate: ")) / 12
months = int(input("Enter Number of Year's: ")) * 12

# Evaluates the futue investment value
f_Value = amount * (1 + interest / 100) ** (months)

# Print's accumulated value for the user
print("The Accumulated Value is", round(f_Value, 2))