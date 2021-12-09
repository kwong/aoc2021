import re

with open("./input.txt", "r") as f:
    data = f.read()
    data = re.findall("([abcdefg\s]+)(?:\| )([abcdefg\s]+)(\n)", data)
    cnt = 0
    for d in data:
        signal = d[0]
        n = d[1]
        n_len = list(map(len, n.strip().split(" ")))
        l_cnt = []
        one_signal = ""
        four_signal = ""
        seven_signal = ""
        eight_signal = ""
        for signal in signal.strip().split(" "):
            # print(signal)
            if len(signal) == 2:
                one_signal = signal
            if len(signal) == 3:
                seven_signal = signal
            elif len(signal) == 4:
                four_signal = signal
            elif len(signal) == 7:
                eight_signal = signal

        partial_five_signal = set(four_signal) - set(one_signal)

        for signal in n.strip().split(" "):
            if len(signal) == 5:  # 2, 3, 5
                if all((c in signal) for c in partial_five_signal):
                    l_cnt.append("5")
                elif all((c in signal) for c in one_signal):
                    l_cnt.append("3")
                else:
                    l_cnt.append("2")
            elif len(signal) == 6:  # 0, 6, 9
                if all((c in signal for c in partial_five_signal)) and all(
                    (c in signal for c in one_signal)
                ):
                    l_cnt.append("9")
                elif all((c in signal for c in partial_five_signal)):
                    l_cnt.append("6")
                else:
                    l_cnt.append("0")
            elif len(signal) == 2:
                l_cnt.append("1")
            elif len(signal) == 3:
                l_cnt.append("7")
            elif len(signal) == 4:
                l_cnt.append("4")
            elif len(signal) == 7:
                l_cnt.append("8")
        cnt += int("".join(l_cnt))
    print(cnt)
