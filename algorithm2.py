# Edit Distance Optimized 

import time

def Edit_Distance_Optimized(word1, word2):
    m, n = len(word1), len(word2)

    prev = list(range(n + 1)) # Previous row
    curr = [0] * (n + 1) # Current row

    for i in range(1, m + 1):
        curr[0] = i # If word2 is empty
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: # If characters are the same, ignore them
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j],      # Insert
                    curr[j - 1],  # Delete
                    prev[j - 1]   # Replace
                )
        prev, curr = curr, prev  # Swap rows

    return prev[n]

def Time(word1, word2):
    start = time.time()
    dist = Edit_Distance_Optimized(word1, word2)
    end = time.time()

    print(word2, "->", word1)
    print("- Optimized Result:")
    print("- Distance:", dist)
    print("- Time Complexity: O(m * n)")
    print("- Space Complexity: O(n)")
    print("- Time:", format(end - start, ".8f"), "seconds") # Display time taken


word1 = "intention"
word2 = "execution"
Time(word1, word2)
