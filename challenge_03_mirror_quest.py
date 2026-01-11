def find_longest_mirror_length(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

   
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Driver code to test the function
print()
print(find_longest_mirror_length("bbabcbcab"))  # Output: 7
print(find_longest_mirror_length("MAPAM"))      # Output: 5
print(find_longest_mirror_length("ABCD"))      # Output: 1
print(find_longest_mirror_length("GEEKS"))     # Output: 3
print()