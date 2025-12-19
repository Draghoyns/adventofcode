from copy import deepcopy

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def load_input(file_path: str) -> list:
    with open(file_path, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.strip("\n")
    return lines


def process_input(input: list) -> list:
    n, m = len(input), len(input[0])
    new_input = []
    mapping = {".": 0, "@": 1, "x": -1}
    for i in range(n):
        new_input.append([])
        for j in range(m):
            new_input[i].append(mapping[input[i][j]])
    return new_input


def rolls_accessible(input: list) -> tuple:
    n, m = len(input), len(input[0])
    valid_roll = 0
    new_input = deepcopy(input)
    for i in range(n):
        for j in range(m):
            roll = input[i][j]
            if roll == 1:
                ul, u, ur = 0, 0, 0
                l, r = 0, 0
                dl, d, dr = 0, 0, 0
                if i != 0:
                    u = input[i - 1][j]
                    if j != 0:
                        ul = input[i - 1][j - 1]
                    if j != n - 1:
                        ur = input[i - 1][j + 1]
                if i != n - 1:
                    d = input[i + 1][j]
                    if j != 0:
                        dl = input[i + 1][j - 1]
                    if j != n - 1:
                        dr = input[i + 1][j + 1]
                if j != 0:
                    l = input[i][j - 1]
                if j != n - 1:
                    r = input[i][j + 1]

                count = sum([cell == 1 for cell in [ul, u, ur, l, r, dl, d, dr]])
                if count < 4:
                    valid_roll += 1
                    new_input[i][j] = -1

    return valid_roll, new_input


def rolls_accessible_remove(input: list) -> int:

    new_count = -1
    total = 0
    new_input = deepcopy(input)

    while new_count != 0:
        new_count, new_input = rolls_accessible(new_input)
        total += new_count
    return total


def test_ex1():
    input = example.split("\n")
    input = process_input(input)
    assert rolls_accessible(input)[0] == 13


def test_ex2():
    input = example.split("\n")
    input = process_input(input)
    assert rolls_accessible_remove(input) == 43


if __name__ == "__main__":

    # test_ex1()

    input_path = "./2025/day4_input.txt"
    input = load_input(input_path)
    input = process_input(input)
    part1, _ = rolls_accessible(input)
    print(part1)

    part2 = rolls_accessible_remove(input)
    print(part2)
