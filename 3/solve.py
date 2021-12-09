def solve1(data):
    gamma = ""
    for i in range(len(data[0]) - 1):  # ignore \n
        count_zero = 0
        count_one = 0
        for j in range(len(data)):

            if data[j][i] == "0":
                count_zero += 1
            else:
                count_one += 1
        if count_zero > count_one:
            gamma += "0"
        else:
            gamma += "1"
    return gamma


def calculate_epsilon(gamma):
    result = ""
    for c in gamma:
        if c == "0":
            result += "1"
        else:
            result += "0"
    return result


def power_consumption(gamma, epsilon):
    return int(gamma, 2) * int(epsilon, 2)


def get_o2(data):
    candidates = data  # consider all at the beginning
    string_size = len(data[0]) - 1
    for i in range(string_size):  # ignore \n
        count_zero = 0
        count_one = 0
        ones_list = []
        zeroes_list = []
        for j in range(len(candidates)):
            if candidates[j][i] == "0":
                count_zero += 1
                zeroes_list.append(candidates[j])
            else:
                count_one += 1
                ones_list.append(candidates[j])
        if count_zero > count_one:
            candidates = zeroes_list
        else:
            candidates = ones_list

        if len(candidates) == 1:
            break
    return candidates[0].strip("\n")


def get_co2(data):
    candidates = data  # consider all at the beginning
    string_size = len(data[0]) - 1
    for i in range(string_size):  # ignore \n
        count_zero = 0
        count_one = 0
        ones_list = []
        zeroes_list = []
        for j in range(len(candidates)):
            if candidates[j][i] == "0":
                count_zero += 1
                zeroes_list.append(candidates[j])
            else:
                count_one += 1
                ones_list.append(candidates[j])
        if count_zero > count_one:
            candidates = ones_list
        else:
            candidates = zeroes_list
        if len(candidates) == 1:
            break
    return candidates[0].strip("\n")


def get_rating(value1, value2):
    return int(value1, 2) * int(value2, 2)


with open("./input.txt", "r") as f:
    content = f.readlines()
    gamma = solve1(content)
    epsilon = calculate_epsilon(gamma)
    print(gamma)
    print(epsilon)
    print(power_consumption(gamma, epsilon))

    # life support rating = oxy rating * c02 scrubber rating
    # oxy rating: most common value in current bit position, 1 as tie break
    # c02: least common, 0 as tie break
    print("---")
    o2 = get_o2(content)
    co2 = get_co2(content)
    print(o2)
    print(co2)
    print(get_rating(o2, co2))
