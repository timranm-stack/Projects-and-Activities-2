def print_time_complexity_analysis():
    print("=== Loop Time Complexity Analysis ===")
    
    # First Loop Analysis
    print("1. First Loop: O(n)")
    print("   - Runs from 0 to n (n + 1 times).")
    print("   - Scales linearly with the input size.")
    
    # Second Loop Analysis
    print("\n2. Second Loop: O(log n)")
    print("   - Variable 'j' doubles in each iteration.")
    print("   - Reaches n + 1 in logarithmic steps.")
    
    # Third Loop Analysis
    print("\n3. Third Loop: O(1)")
    print("   - Always runs exactly 100 times.")
    print("   - Independent of the input size 'n'.")
    
    # Total Complexity
    print("\n" + "="*37)
    print("Total Time Complexity: O(n)")
    print("="*37)
    print("Reason: O(n) + O(log n) + O(1) simplifies to O(n) as it is the dominant term.")

if __name__ == "__main__":
    print_time_complexity_analysis()