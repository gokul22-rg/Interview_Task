
#4 - Here is a function to test whether a number is prime or not.
   # Write a few test cases for this function to see if you can catch any errors in the implementation.



import math


def isprime(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(7, math.floor(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


# Test case 1: The below line returns math domain error.Exception Handling is not Implemented.
print(isprime(-7))

# Test case 2: The below line returns False
print(isprime(2))

# Test case 3: The below line returns False
print(isprime(3))

# Test case 4: The below line returns False
print(isprime(5))
