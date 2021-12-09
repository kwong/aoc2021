# def maketuple(data):
def get_dimensions(data):
    max_x = 0
    max_y = 0
    for d in data:
        # for tup in d:
        x1 = int(d[0][0])
        x2 = int(d[1][0])
        y1 = int(d[0][1])
        y2 = int(d[1][1])
        x_from = min(x1, x2)
        x_to = max(x1, x2)
        y_from = min(y1, y2)
        y_to = max(y1, y2)
        if max_x < x_to:
            max_x = x_to
        if max_y < y_to:
            max_y = y_to
            # print(x1, y1, x2, y2)
            # print(max_x, max_y)
    return max_x, max_y


def generate_template(max_x, max_y):
    board = []
    for i in range(max_y + 1):
        board.append([])
        for j in range(max_x + 1):
            board[i].append(".")
    return board


def fill(data, template):

    result = template
    # bprint(result)
    for d in data:
        x1 = int(d[0][0])
        x2 = int(d[1][0])
        y1 = int(d[0][1])
        y2 = int(d[1][1])
        x_from = min(x1, x2)
        x_to = max(x1, x2)
        y_from = min(y1, y2)
        y_to = max(y1, y2)
        # print(x1, y1, x2, y2)
        # print(max_x, max_y)
        if x1 != x2 and y1 != y2:
            # continue
            if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
                ypos = y_from
            else:
                ypos = y_to
            for j in range(x_from, x_to + 1):
                # print(d, "d", j, ypos)
                if result[ypos][j] == ".":
                    result[ypos][j] = "1"
                else:
                    result[ypos][j] = str(1 + int(result[ypos][j]))
                if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
                    ypos = ypos + 1
                else:
                    ypos = ypos - 1
        else:
            for j in range(x_from, x_to + 1):
                for i in range(y_from, (y_to + 1)):

                    # print(i, j)
                    if result[i][j] == ".":
                        result[i][j] = "1"
                    else:
                        result[i][j] = str(1 + int(result[i][j]))
    # bprint(result)
    return result


def bprint(b):
    for line in b:
        print(line)


def countpoints(b):
    count = 0
    for p in [item for sublist in b for item in sublist]:
        if p != "." and int(p) > 1:
            count += 1
    return count


with open("./example_input.txt", "r") as f:
    content = f.read()

    data = list(
        map(lambda line: line.split(" -> "), content.splitlines())
    )  # content.split("->")
    data = list(map(lambda x: (x[0].split(","), x[1].split(",")), data))

    dimensions = get_dimensions(data)
    # print(dimensions)
    template = generate_template(*dimensions)
    filled = fill(data, template)
    bprint(filled)
    print(countpoints(filled))
