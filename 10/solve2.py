from statistics import median

with open("./input.txt", "r") as f:
    data = f.read()

S = {"{": "}", "<": ">", "[": "]", "(": ")"}
chart = []

for line in data.splitlines():
    stack = []
    corrupted = False
    for c in line:
        if c in S.keys():
            stack.append(c)
        if c in S.values():
            last = stack.pop()
            if S.get(last) != c:
                corrupted = True
    if not corrupted:
        score = 0
        while len(stack) > 0:
            t = stack.pop()
            if t == "(":
                score = (score * 5) + 1
            if t == "[":
                score = (score * 5) + 2
            if t == "{":
                score = (score * 5) + 3
            if t == "<":
                score = (score * 5) + 4
        chart.append(score)
# print(chart)
print(median(chart))
