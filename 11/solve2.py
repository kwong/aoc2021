with open("./input.txt", "r") as f:
    data = f.read()

flashes = 0


def step(X, i, j, store):
    global flashes
    if (i, j) not in store:
        X[i][j] += 1
    if X[i][j] <= 9:
        return
    else:
        X[i][j] = 0
        store.add((i, j))
        flashes += 1
        # print(f"{i, j} flashed")
        if i > 0:
            step(X, i - 1, j, store)  # u

        if i > 0 and j > 0:
            step(X, i - 1, j - 1, store)  # ul

        if i > 0 and (j < len(X[0]) - 1):
            step(X, i - 1, j + 1, store)  # ur

        if i < len(X) - 1:
            step(X, i + 1, j, store)

        if i < len(X) - 1 and j > 0:
            step(X, i + 1, j - 1, store)

        if i < len(X) - 1 and j < len(X[0]) - 1:
            step(X, i + 1, j + 1, store)

        if j < len(X[0]) - 1:
            step(X, i, j + 1, store)

        if j > 0:
            step(X, i, j - 1, store)


def prettyprint(X, step):
    print(f"step {step}")
    for x in X:
        print(x, "\n")
    print("----------")


def allflashed(X):
    return sum(list(map(sum, X))) == 0


X = []
for x in data.splitlines():
    X.append([int(i) for i in x])

steps = 0
while not allflashed(X):
    store = set()
    for i in range(len(X)):
        for j in range(len(X[0])):
            step(X, i, j, store)
            # print(store)
    steps = steps + 1
    prettyprint(X, steps)

print(steps)
