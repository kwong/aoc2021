import sys

with open("./input.txt", "r") as f:
    data = f.read()
    data = list(map(int, data.split(",")))
    # print(data)

    lowest_cost = sys.maxsize
    for pos in range(min(data), max(data)):
        cost = 0
        for x in data:
            n = abs(x - pos)
            cost = cost + (n * ((n + 1) / 2))
        if cost < lowest_cost:
            lowest_cost = cost

    print(lowest_cost)
