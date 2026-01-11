def can_balance_scales(arr):
    total_sum = sum(arr)

    # Parity check
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for weight in arr:
        for s in range(target, weight - 1, -1):
            if dp[s - weight]:
                dp[s] = True

    return dp[target]


#Driver code to test the function

if __name__ == "__main__":
    # Test Case 1
    arr1 = [[1,5,11,5],[1,3,5],[2,2,2,2]]
    print()
    for arr in arr1:
        print("Input:", arr)
        print("Can balance scales?", can_balance_scales(arr))
        print()