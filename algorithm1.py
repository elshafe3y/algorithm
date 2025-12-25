# Edit Distance Naive 

import time

def Edit_Distance_Naive(w1, w2, m, n):
    
    if m == 0: 
        return n # If w1 is empty
    if n == 0: 
        return m # If w2 is empty

    if w1[m-1] == w2[n-1]: # If characters are the same, ignore them
        return Edit_Distance_Naive(w1, w2, m-1, n-1)

    return 1 + min(
        Edit_Distance_Naive(w1, w2, m, n-1),    # Insert
        Edit_Distance_Naive(w1, w2, m-1, n),    # Delete
        Edit_Distance_Naive(w1, w2, m-1, n-1)   # Replace
    )

def Time(word1, word2):
    
    start = time.time() 
    result = Edit_Distance_Naive(word1, word2, len(word1), len(word2))
    end = time.time()

    print(word2, "->", word1)
    print("- Naive Result:")
    print("- Distance:",result)
    print("- Time Complexity: O(3^(m+n))")
    print("- Space Complexity: O(m + n)")
    print("- Time:", format(end - start, '.8f'),"seconds") # Display time taken

word1 = "intention"
word2 = "execution"
Time(word1, word2)
