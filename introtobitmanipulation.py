def to_binary_string(number, bits=8):
    """Goal 1: Represent decimal numbers in binary using a helper function."""
    # Formats the number as a binary string padded with leading zeros
    return f"{number:0{bits}b}"

def scan_secret_code(secret_code, access_key):
    print("=== SECRET CODE BIT SCANNER ===")
    print(f"Secret Code (Decimal): {secret_code} -> Binary: {to_binary_string(secret_code)}")
    print(f"Access Key  (Decimal): {access_key} -> Binary: {to_binary_string(access_key)}")
    print("-" * 40)

    # Goal 2: Use AND and OR to compare binary values bit by bit
    bit_and = secret_code & access_key
    bit_or = secret_code | access_key
    print(f"Bitwise AND (Matching 1s):  {to_binary_string(bit_and)} (Decimal: {bit_and})")
    print(f"Bitwise OR  (Combined 1s):  {to_binary_string(bit_or)} (Decimal: {bit_or})")

    # Goal 3: Use NOT and XOR to flip bits and find differences between codes
    # Mask to keep it to an 8-bit inversion for display
    bit_not_secret = ~secret_code & 0xFF 
    bit_xor = secret_code ^ access_key
    print(f"Bitwise NOT (Flipped Code): {to_binary_string(bit_not_secret)} (Decimal: {bit_not_secret})")
    print(f"Bitwise XOR (Differences):  {to_binary_string(bit_xor)} (Decimal: {bit_xor})")

    # Goal 4: Apply left shift and right shift to move binary values
    shift_left = secret_code << 2
    shift_right = secret_code >> 2
    print(f"Left Shift Code by 2:      {to_binary_string(shift_left, 10)} (Decimal: {shift_left})")
    print(f"Right Shift Code by 2:     {to_binary_string(shift_right)} (Decimal: {shift_right})")

    # Goal 5: Use XOR logic to check whether a number is odd or even
    # xor with 1 flips the last bit. If result < number, the last bit was 1 (odd).
    is_odd_xor = (secret_code ^ 1) < secret_code
    parity = "Odd" if is_odd_xor else "Even"
    print(f"Parity Check (using XOR):   The secret code is {parity}")

    # Goal 6: Count the number of 1 bits in a value using bit_count()
    # Note: int.bit_count() requires Python 3.10 or newer
    ones_count = secret_code.bit_count()
    print(f"Bit Count (1s in Code):    {ones_count}")
    print("=" * 40)

# --- Execute Project Template ---
# Example inputs (Secret Code = 42, Access Key = 15)
scan_secret_code(42, 15)