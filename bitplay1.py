# Goal 6: Connect bit positions to real smart switch states (0-indexed from right)
SWITCHES = {
    0: "Living Room Light",
    1: "Kitchen Fan",
    2: "Security Camera",
    3: "Air Conditioner",
    4: "Garage Door",
    5: "Smart Lock",
    6: "Garden Sprinkler",
    7: "Water Heater"
}

def display_binary(number, bits=8):
    """Goal 1: Understand set bits as 1s and zero bits as 0s in a binary number."""
    return f"{number:0{bits}b}"

def count_set_bits(number):
    """Goal 2: Count the number of set bits using loops, AND, and right shift."""
    count = 0
    temp = number
    while temp > 0:
        # Check if the rightmost bit is 1 (set)
        if (temp & 1) == 1:
            count += 1
        # Shift right by 1 to check the next bit
        temp = temp >> 1
    return count

def find_first_set_bit(number):
    """Goal 3: Find the first set bit (1-indexed position) from the right side."""
    if number == 0:
        return None  # No set bits
    
    position = 1
    while number > 0:
        if (number & 1) == 1:
            return position
        number = number >> 1
        position += 1
    return None

def check_nth_bit(number, n):
    """Goal 4 & 5: Build bit masks using left shift and check if the nth bit is set."""
    # Build the mask by shifting 1 left by n positions
    mask = 1 << n
    
    # Check if the bit is set using bitwise AND
    return (number & mask) != 0

def monitor_smart_switches(switch_register):
    print("=== MY SMART SWITCH BIT MONITOR ===")
    print(f"Current Register Value: {switch_register}")
    print(f"Binary Representation:  {display_binary(switch_register)}")
    print("-" * 45)
    
    # Goal 2 Output
    total_on = count_set_bits(switch_register)
    print(f"Total Switches turned ON: {total_on}")
    
    # Goal 3 Output
    first_on = find_first_set_bit(switch_register)
    print(f"First active switch position from right: {first_on}")
    print("-" * 45)
    
    # Goal 5 & 6 Output: Inspecting every appliance status
    print("Device Status Report:")
    for position, device_name in SWITCHES.items():
        # Check if the bit at this position is set
        is_on = check_nth_bit(switch_register, position)
        status = "ON (1)" if is_on else "OFF (0)"
        print(f"  Bit {position} -> {device_name:<20} : {status}")
    print("=" * 45)

# --- Execute Project Template ---
# Example: 0b00101011 in decimal is 43
# This means bits 0, 1, 3, and 5 are ON
smart_home_state = 43
monitor_smart_switches(smart_home_state)