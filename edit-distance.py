# Simple edit Distance

def editDistance(str1, str2, m, n):
    
    # return remain char length
    if m==0: return n
    if n==0: return m
    
    # same char --> check from end
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    
    # diff char
    return 1 + min(
        editDistance(str1, str2, m, n-1), # Insert
        editDistance(str1, str2, m-1, n), # Delete
        editDistance(str1, str2, m-1, n-1) #replace
    )

st1 = "mate"
st2 = "bat"

print("edit distance: ", editDistance(st1, st2, len(st1), len(st2)))


# weight edit distance
import numpy as np

def weightEditDistance( s1, s2):
    size_x, size_y = len(s1)+1, len(s2)+1
    dp = np.zeros((size_x, size_y), dtype=int)
    
    for x in range(size_x)    