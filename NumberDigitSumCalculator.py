# Read's the input from the user
n = int(input("Please Enter A Number Between 0 And 1000: "))

# Evaluates the numbers
a = n // 1000
b = (n - a * 1000) // 100
c = (n - a * 1000 - b * 100) // 10
d = n - a * 1000 - b * 100 - c * 10

# Add's the summ of all the digits 
# in the number and print's them for the user
print("The Sum Of All The Digits In The Number is", a + b + c + d)