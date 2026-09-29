n = int(input("Enter N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total_sum = n * (n + 1) // 2
    print(f"The sum of first {n} natural numbers is {total_sum}.")