def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask the user for number of terms
n_terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
