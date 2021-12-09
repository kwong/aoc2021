with open("./input.txt", "r") as f:
    data = f.read()

import sys


def islowest(X, i, j):
    u = int(X[i - 1][j]) if i > 0 else sys.maxsize
    d = int(X[i + 1][j]) if i < (len(X) - 1) else sys.maxsize
    r = int(X[i][j + 1]) if j < (len(X[0]) - 1) else sys.maxsize
    l = int(X[i][j - 1]) if j > 0 else sys.maxsize
    c = int(X[i][j])

    return c < u and c < d and c < l and c < r


def find_higher(X, i, j, found):
    u = int(X[i - 1][j]) if i > 0 else 9
    d = int(X[i + 1][j]) if i < (len(X) - 1) else 9
    r = int(X[i][j + 1]) if j < (len(X[0]) - 1) else 9
    l = int(X[i][j - 1]) if j > 0 else 9
    c = int(X[i][j])

    if c == 9 or ((i, j) in found):
        return

    found.append((i, j))
    if u > c and u != 9:
        find_higher(X, i - 1, j, found)

    if d > c and d != 9:
        find_higher(X, i + 1, j, found)

    if r > c and r != 9:
        find_higher(X, i, j + 1, found)

    if l > c and l != 9:
        find_higher(X, i, j - 1, found)


X = [x for x in data.splitlines()]

found = []
for i in range(len(X)):
    for j in range(len(X[0])):
        if islowest(X, i, j):
            f = []
            find_higher(X, i, j, f)
            found.append(len(f))

found = sorted(found)
print(found[-1] * found[-2] * found[-3])
