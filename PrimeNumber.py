def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False  # 1 or less are not prime
    for i in range(2, int(num**0.5) + 1):  # Iterate up to the square root
        if num % i == 0:
            return False  # Divisible by a number other than 1 or itself
    return True  # If no divisors found, it's prime

entery = int(input("Enter a number: "))
prime_numbers = []
for num in range(3, entery):
    if is_prime(num):
        prime_numbers.append(num)

if prime_numbers:
    print("Prime numbers less than", entery, "are:", prime_numbers)
else:
    print("There are no prime numbers less than", entery)
