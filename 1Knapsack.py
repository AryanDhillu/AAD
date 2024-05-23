def knapSack(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # stores the result of Knapsack
    res = K[n][W]

    w = W
    solution_vector = [0] * n
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included.
            solution_vector[i - 1] = 1
            res -= val[i - 1]
            w -= wt[i - 1]

    return solution_vector


if __name__ == '__main__':
    weight = [int(x) for x in input("Enter weights separated by space: ").split()]
    profit = [int(x) for x in input("Enter values separated by space: ").split()]
    W = int(input("Enter the capacity of knapsack: "))
    n = len(profit)
    solution = knapSack(W, weight, profit, n)
    print("Solution vector:", solution)
