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

piles = [5, 10, 3]
k = 4
print(calculate_minimum_speed(piles, k))  # Output: 5