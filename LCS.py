def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0, ""
    elif X[m - 1] == Y[n - 1]:
        length, sequence = lcs(X, Y, m - 1, n - 1)
        return length + 1, sequence + X[m - 1]
    else:
        length1, sequence1 = lcs(X, Y, m, n - 1)
        length2, sequence2 = lcs(X, Y, m - 1, n)
        if length1 > length2:
            return length1, sequence1
        else:
            return length2, sequence2


S1 = input("Enter the First String: ")
S2 = input("Enter the Second String: ")
length, sequence = lcs(S1, S2, len(S1), len(S2))
print("Length of LCS is", length)
print("Longest Common Subsequence is", sequence)
