import numpy as np

example = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]


def load_input(file_path: str):
    with open(file_path, "r") as f:
        banks = f.readlines()

    for i in range(len(banks)):
        banks[i] = banks[i][:-1]
    return banks


def output_joltage(banks: list) -> int:

    total_joltage = 0
    for bank in banks:
        # get first max digit
        max_bank = 0
        max_idx = 0
        for idx, num in enumerate(bank):
            if int(num) > max_bank and idx != len(bank) - 1:
                max_bank = int(num)
                max_idx = idx
        second_digit = -1
        for idx in range(max_idx + 1, len(bank)):
            if int(bank[idx]) > second_digit:
                second_digit = int(bank[idx])

        joltage = int(str(max_bank) + str(second_digit))
        total_joltage += joltage

    return total_joltage


def optimize_bank(bank: str, on_off: list) -> list:
    if len(set(on_off)) == 1:
        return on_off

    first_digit_idx = 0
    while on_off[first_digit_idx] == 0:
        first_digit_idx += 1

    first_digit = bank[first_digit_idx]

    max_first = 0
    max_idx = first_digit_idx
    for idx in range(first_digit_idx):
        digit = int(bank[idx])
        if digit > max_first:
            max_first = digit
            max_idx = idx

    if max_first >= int(first_digit):
        on_off[first_digit_idx] = 0
        on_off[max_idx] = 1

    next_on_off = optimize_bank(bank[max_idx + 1 :], on_off[max_idx + 1 :])

    return on_off[: max_idx + 1] + next_on_off


def output_joltage_12digits(banks: list) -> int:
    total_joltage = 0
    for bank in banks:
        n = len(bank)
        on_off = [0] * (n - 12) + [1] * (12)

        # optimize joltage
        on_off = optimize_bank(bank, on_off)

        # get output joltage for the bank
        aggregate = [on_off[i] * int(bank[i]) for i in range(n)]
        lit_joltage = ""
        for digit in aggregate:
            if digit != 0:
                lit_joltage += str(digit)
        joltage = int(lit_joltage)

        total_joltage += joltage

    return total_joltage


def test_ex1():
    assert output_joltage(example) == 357


def test_ex2():
    assert output_joltage_12digits(example) == 3121910778619


if __name__ == "__main__":
    input_path = "./2025/day3_input.txt"
    input = load_input(input_path)

    part1 = output_joltage(input)
    print(part1)

    part2 = output_joltage_12digits(input)
    print(part2)
