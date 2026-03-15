# Armstrong number checker

# Get input from the user
num = int(input("Enter a number: "))

# Convert number to string to easily get number of digits
num_str = str(num)
n = len(num_str)

# Calculate the sum of each digit raised to the power n
armstrong_sum = 0
for digit in num_str:
    armstrong_sum += int(digit) ** n

# Check and print result
if armstrong_sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
