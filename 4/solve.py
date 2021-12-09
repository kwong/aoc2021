def parse_boards(data):
    # board_len = len(data[0])
    boards = []  # board is a list of lists
    board = []
    for i in range(len(data)):
        if data[i] == "\n":
            boards.append(board)
            board = []
            continue
        data[i].split(" ")
        row = list(
            filter(lambda n: True if n is not "" else False, data[i].strip().split(" "))
        )
        # print(row)
        board.append(row)
    return boards


def print_boards(boards):
    for board in boards:
        for row in board:
            print(f"{row}")
        print("\n")


def play(board, calls):
    # get next call number
    marks = []
    steps = 0
    for call in calls:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == call:
                    marks.append(i * len(board) + j)
                    if bingo(marks):
                        return (
                            sorted(marks),
                            len(marks),
                            board_score(marks, board, int(call)),
                            steps,
                        )
        steps += 1
    return None


def bingo(board_marks):
    if (
        0 in board_marks
        and 1 in board_marks
        and 2 in board_marks
        and 3 in board_marks
        and 4 in board_marks
    ):
        return True
    if (
        5 in board_marks
        and 6 in board_marks
        and 7 in board_marks
        and 8 in board_marks
        and 9 in board_marks
    ):
        return True
    if (
        10 in board_marks
        and 11 in board_marks
        and 12 in board_marks
        and 13 in board_marks
        and 14 in board_marks
    ):
        return True
    if (
        15 in board_marks
        and 16 in board_marks
        and 17 in board_marks
        and 18 in board_marks
        and 19 in board_marks
    ):
        return True
    if (
        20 in board_marks
        and 21 in board_marks
        and 22 in board_marks
        and 23 in board_marks
        and 24 in board_marks
    ):
        return True

    # COLS
    if (
        0 in board_marks
        and 5 in board_marks
        and 10 in board_marks
        and 15 in board_marks
        and 20 in board_marks
    ):
        return True
    if (
        1 in board_marks
        and 6 in board_marks
        and 11 in board_marks
        and 16 in board_marks
        and 21 in board_marks
    ):
        return True

    if (
        2 in board_marks
        and 7 in board_marks
        and 12 in board_marks
        and 17 in board_marks
        and 22 in board_marks
    ):
        return True

    if (
        3 in board_marks
        and 8 in board_marks
        and 13 in board_marks
        and 18 in board_marks
        and 23 in board_marks
    ):
        return True

    if (
        4 in board_marks
        and 9 in board_marks
        and 14 in board_marks
        and 19 in board_marks
        and 24 in board_marks
    ):
        return True

    return False


def board_score(marks, board, call):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if i * len(board) + j not in marks:
                sum += int(board[i][j])

    # print(f"{sum} * {call}")
    return sum * call


calls = []
boards = []

with open("./calls.txt", "r") as f:
    content = f.readlines()
    calls = str(content[0]).split(",")

with open("./boards.txt", "r") as f:
    content = f.readlines()
    boards = parse_boards(content)
    # print_boards(boards)
    results = []
    for board in boards:
        results.append(play(board, calls))

    results.sort(key=(lambda elem: elem[3]))
    # print(results[0])
    # for i in range(len(results)):
    #     print(i, results[i])
    #     print("\n")

    print("Answer for 1:", results[0][-2])
    print("Answer for 2:", results[-1][-2])

# with open("./example_input.txt", "r") as f:
#     data = f.read()
#     data = data.split("\n\n")
#     calls = data[0].split(",")
#     # print(calls)
#     boards = list(map(lambda x: x.split("\n"), data[1:]))
#     boards =
#     boards = parse_boards(data[1:])
#     print_boards(boards)
