#Knapsack problem
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        if wt[i - 1] <= w:
            dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print("Max value:", dp[n][W])

items = []
w = W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        items.append(i)
        w -= wt[i - 1]

print("Items taken:", items[::-1])