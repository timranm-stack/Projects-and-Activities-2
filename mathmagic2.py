def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find all 2-digit prime numbers (from 10 to 99)
two_digit_primes = [num for num in range(10, 100) if is_prime(num)]

# Print the results
print("The 2-digit prime numbers are:")
print(two_digit_primes)
print(f"\nTotal count: {len(two_digit_primes)}")