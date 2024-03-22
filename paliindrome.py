def is_palindrome(number):
  """Checks if a number is a palindrome (reads the same backward as forward)."""

  # Handle negative numbers (not palindromes)
  if number < 0:
    return False

  # Efficiently check characters from start and end
  for i in range(len(str(number)) // 2):
    if str(number)[i] != str(number)[-1 - i]:
      return False

  return True  # If no mismatches found, it's a palindrome

# Example usage
l = int(input("Enter a number: "))

if is_palindrome(l):
  print(l, "is a palindrome")
else:
  print(l, "is not a palindrome")
