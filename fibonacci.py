def f(limit):
    """Calculates the Fibonacci sequence up to the given limit and prints the sum of even numbers."""

    a = 1
    e = 0
    z = 0  # Initialize z to 0 outside the loop to store the sum of even numbers

    while k < limit:
        k = a + e
        e = a
        a = k
        print(k)
        if k % 2 == 0:
            z += k  # Add even numbers to the sum

    print("Sum of even numbers:", z)  # Print the total sum of even numbers after the loop

while True:
    try:
        while True:  # Inner loop for repeated input until valid number
            limit = int(input("Enter the border value (or 0 to quit): "))

            if limit == 0:
                break  # Exit the inner loop if user enters 0
            f(limit)  # Call the function with the valid limit
            break  # Exit the inner loop after a successful call

    except ValueError:
        print("Invalid input. Please enter a number: ")
