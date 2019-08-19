# Ask user to input a number
num = int(input("Enter a number: "))

# A number is even if division by 2 gives a remainder of 0.
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
