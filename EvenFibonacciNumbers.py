def f(l):
    a = 1
    e = 0
    k=0
    z = 0  # Initialize z to 0 outside the loop to store the sum of even numbers
    while (k < l):
        k = a + e
        e = a
        a = k
        print(k)
        if (k % 2 == 0):
            z += k  # Add even numbers to the sum

    print("Sum of even numbers:", z)  # Print the total sum of even numbers after the loop

while True:
    
       try:
         l=int(input("ennter the border value"))
         print("if you wont to break enter 0")
         if (l==0):
            break
         f(l)
       except ValueError:
         print("Invalid input. Please enter a number: ")
