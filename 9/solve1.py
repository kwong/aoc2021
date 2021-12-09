with open("./input.txt", "r") as f:
    data = f.read()

import sys


def islowest(X, i, j):
    # X[i][j]
    try:
        u = int(X[i - 1][j]) if i > 0 else sys.maxsize
        d = int(X[i + 1][j]) if i < (len(X) - 1) else sys.maxsize
        r = int(X[i][j + 1]) if j < (len(X[0]) - 1) else sys.maxsize
        l = int(X[i][j - 1]) if j > 0 else sys.maxsize
    except IndexError:
        pass
    return (
        int(X[i][j]) < u and int(X[i][j]) < d and int(X[i][j]) < l and int(X[i][j]) < r
    )


X = []
for x in data.splitlines():
    X.append(x)

sum = 0
for i in range(len(X)):
    for j in range(len(X[0])):
        if islowest(X, i, j):
            print(f"{X[i][j]} is lowest")
            sum += int(X[i][j]) + 1
print(sum)
