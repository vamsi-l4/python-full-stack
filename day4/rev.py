def reverse_number(N):
    return int(str(N)[::-1])  # Convert to string, reverse, and convert back to integer

# Example usage
N = int(input("Enter a number: "))
print(reverse_number(N))
