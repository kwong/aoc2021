# lanternfish spawn at 1 per 7 days 0..6
# fish has timer (0..6) to create new lanternfish
# new lanternfish need 7+2 days in first cycle to create new fish
### All new fish start with 8
from collections import defaultdict, Counter


class Fish:
    def __init__(self, timer=9):
        self.timer = timer

    def __str__(self):
        return str(self.timer)

    def spawned_new(self):
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            self.timer = self.timer - 1
        return False


def list_fishes(fishes):
    l = ""
    for fish in fishes:
        l += str(fish) + ","
    return l


days = 18


def process(X, days):
    temp = X
    for i in range(days):
        y = defaultdict(int)
        for x, cnt in temp.items():
            if x == 0:
                y[8] = cnt
                y[6] += cnt
            else:
                y[x - 1] += cnt
        temp = y
    return sum(temp.values())


with open("./input.txt", "r") as f:
    data = f.read()
    data = list(map(int, data.split(",")))
    # fishes = list(map(Fish, data))
    X = Counter(data)
    print(process(X, days))

    # for days in range(1, days + 1):
    #     for fish in fishes:
    #         if fish.spawned_new():
    #             new_fish = Fish()
    #             fishes.append(new_fish)
    # entire_school = 0
    # for fish in fishes:
    #     entire_school += len(process(days, [fish]))

    # # print(f"After {days} Days: {list_fishes(fishes)}")
    # # print(f"Total fish = {len(fishes)}")
    # print(f"Total fish = {entire_school}")
