from collections import Counter
import re


with open("./input.txt", "r") as f:
    data = f.read()
    data = re.findall("([abcdefg\s]+)(?:\| )([abcdefg\s]+)(\n)", data)
    cnt = 0
    for d in data:
        signal = d[0]
        n = d[1]
        n_len = list(map(len, n.strip().split(" ")))
        X = Counter([int(x) for x in n_len])
        cnt += X[2] + X[4] + X[3] + X[7]

    print(cnt)
