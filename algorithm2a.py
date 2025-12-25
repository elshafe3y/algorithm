# Edit Distance Optimized with Backtracking

import time

def edit_distance_with_Backtracking(word1, word2):
    m, n = len(word1), len(word2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)] # DP table

    for i in range(m + 1):
        dp[i][0] = i # If word2 is empty
    for j in range(n + 1):
        dp[0][j] = j # If word1 is empty

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: # If characters are the same, ignore them
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # Insert
                    dp[i][j - 1],     # Delete
                    dp[i - 1][j - 1]  # Replace
                )

    steps = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]: # Characters are the same
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1: # Replace
            steps.append(f"Replace '{word2[j-1]}' with '{word1[i-1]}'") #Display replace operation
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1: # Insert
            steps.append(f"Insert '{word1[i-1]}'") #Display insert operation
            i -= 1
        else: # Delete
            steps.append(f"Delete '{word2[j-1]}'") #Display delete operation
            j -= 1

    steps.reverse()
    return dp[m][n], steps

def Time(word1, word2):
    start = time.time()
    dist, operations = edit_distance_with_Backtracking(word1, word2)
    end = time.time()

    print(word2, "->", word1)
    print("- Optimized with Backtracking Result:")
    print("- Distance:", dist)
    print("- Operations:")
    for op in operations:
        print("-", op)
    print("- Time Complexity: O(m * n)")
    print("- Space Complexity: O(m * n)")
    print("- Time:", format(end - start, ".8f"), "seconds")

word1 = "intention"
word2 = "execution"
Time(word1, word2)