# Prompt user for input
number = int(input("Enter a number: "))

# Check if the number is divisible by 2
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")