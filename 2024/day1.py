import numpy as np


def load_data(file_path: str) -> tuple:

    with open(file_path, "r") as file:
        lines = file.readlines()
    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    return left, right


def sum_diff(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    L = np.array(left)
    R = np.array(right)
    diff = np.abs(L - R)
    return sum(diff)


def similarity_score(left: list[int], right: list[int]) -> int:
    freq_dict = {}
    score = 0
    for r in right:
        freq_dict[r] = freq_dict.get(r, 0) + 1

    for l in left:
        incr = l * freq_dict.get(l, 0)
        score += incr

    return score


def part1_ex():
    l = [3, 4, 2, 1, 3, 3]
    r = [4, 3, 5, 3, 9, 3]

    res = sum_diff(l, r)
    correct = 11

    if res == correct:
        print("Test case passed.")
    else:
        print("Something went wrong. Debug your code.")


def part2_ex():
    l = [3, 4, 2, 1, 3, 3]
    r = [4, 3, 5, 3, 9, 3]

    res = similarity_score(l, r)
    correct = 31

    if res == correct:
        print("Test case passed.")
    else:
        print("Something went wrong. Debug your code.")


if __name__ == "__main__":

    part1_ex()
    part2_ex()
    l, r = load_data("2024/day1_input.txt")

    print(f"Result: {sum_diff(l,r)}")
    print(f"Result: {similarity_score(l,r)}")
