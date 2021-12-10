# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

with open("./input.txt", "r") as f:
    data = f.read()


S = {"{": "}", "<": ">", "[": "]", "(": ")"}


score = 0
for line in data.splitlines():
    stack = []
    for c in line:
        if c in S.keys():
            stack.append(c)
        if c in S.values():
            # print(stack)
            last = stack.pop()
            if S.get(last) != c:
                if c == ")":
                    score += 3
                if c == "]":
                    score += 57
                if c == "}":
                    score += 1197
                if c == ">":
                    score += 25137
                print(f"expected {S.get(last)} found {c}")

print(score)
