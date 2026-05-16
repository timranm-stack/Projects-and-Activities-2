def multiply_one_iteration(a, b):
    # Direct multiplication completes in 1 operational step
    return a * b

def multiply_n_iterations(a, b):
    # Repeated addition loops exactly 'b' (N) times
    result = 0
    for _ in range(b):
        result += a
    return result

# User input
a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

# Display results
print(f"\n1 iteration: {multiply_one_iteration(a, b)}")
print(f"N iteration: {multiply_n_iterations(a, b)}")