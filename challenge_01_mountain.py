def count_ways_to_summit(n) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

print()
print(count_ways_to_summit(4))  # Example usage
print(count_ways_to_summit(45))  # Example usage
print()