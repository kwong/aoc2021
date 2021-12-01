def sliding_window_list(data, s=3):
    new_list = []
    for i in range(0, len(data)-2):
        new_list += [data[slice(i, i+s)]]
    return new_list


def sum_lists(data):
    new_list = []
    for r in data:
        #print(r)
        new_list += [sum(r)]

    return new_list

def count_positive_increment(data):
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1
    return count


with open("./input.txt", "r") as f:
    content = f.readlines()
    data = [int(i) for i in content]

    #A
    print(count_positive_increment(data))

    #B
    list_1 = sliding_window_list(data)
    list_2 = sum_lists(list_1)
    print(count_positive_increment(list_2))

