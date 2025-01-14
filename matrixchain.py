def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")

# Get matrix dimensions from user input
n = int(input("Enter the number of matrices: "))
matrix_dimensions = []
for i in range(n + 1):
    dim = int(input(f"Enter dimension {i + 1}: "))
    matrix_dimensions.append(dim)

print("Matrix dimensions:", matrix_dimensions)
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of scalar multiplications:", m[0][n - 1])
print("Optimal parenthesization:", end="")
print_optimal_parens(s, 0, n - 1)

