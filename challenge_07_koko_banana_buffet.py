def calculate_minimum_speed(piles, k):
    left, right = 1, max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        hours_needed = 0

        for pile in piles:
            # Equivalent to ceil(pile / mid)
            hours_needed += (pile + mid - 1) // mid

        if hours_needed <= k:
            answer = mid         
            right = mid - 1
        else:
            left = mid + 1       

    return answer

# Example 1
piles = [5, 10, 3]
k = 4
print("Output 1:", calculate_minimum_speed(piles, k))  # Output: 5

# Example 2
piles2 = [5, 10, 15, 20]
k2 = 7
print("Output 2:", calculate_minimum_speed(piles2, k2)) # Output: 8