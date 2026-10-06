try:
    #  Take input from the user
    first = int(input("Enter the first starting number: "))
    second = int(input("Enter the second starting number: "))
    n = int(input("Enter the total number of terms (N): "))

    # Handle cases based on the value of N
    if n <= 0:
        print("Please enter a positive integer for N.")
    elif n == 1:
        print(f"\nThe sequence with 1 term is:\n[{first}]")
    else:
        # Initialize the list with the first two numbers
        sequence = [first, second]

        # Loop from 2 to N-1 to generate the remaining terms
        for _ in range(2, n):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)

        # 3. Display the final result
        print(f"\nThe sequence with {n} terms is:")
        print(sequence)

except ValueError:
    print("Invalid input! Please enter integers only.")