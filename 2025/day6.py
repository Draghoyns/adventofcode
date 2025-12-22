import numpy as np

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def load_input(file_path: str) -> list:
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


def process_input(input):
    # modify if necessary
    ope_matrix = []

    for row in input:
        row = row.strip("\n")
        list_str = [c for c in row]

        ope_matrix.append(list_str)

    shape = len(ope_matrix), len(ope_matrix[0])

    np_matrix = np.array(ope_matrix).reshape(shape).transpose()

    return np_matrix


# TODO : write the main function
def main_part1(input: np.ndarray) -> int:
    m, n = input.shape
    grand_total = 0

    # I erased it but it worked

    return grand_total


def main_part2(input: np.ndarray) -> int:
    m, n = input.shape
    grand_total = 0

    idx = 0
    while idx < m:
        operation = " "
        one_problem = []
        while (operation == " " or idx == 0) and idx < m:
            row = input[idx]
            one_problem.append(row.tolist())
            idx += 1
            operation = input[idx, -1] if idx < m else " "

        if set(one_problem[-1]) == {" "}:
            one_problem.pop()

        numbers = []
        operation = one_problem[0][-1].strip()
        for row in one_problem:
            number = "".join(row[:-1])
            numbers.append(int(number))
        if operation == "+":
            row_total = sum(numbers)
        else:  # operation == '*'
            row_total = 1
            for nb in numbers:
                row_total *= nb

        grand_total += row_total

    return grand_total


def test_ex1():
    # TODO
    input_example = example.split("\n")
    input = process_input(input_example)
    part1 = main_part1(input)
    assert part1 == 4277556


def test_ex2():
    # TODO
    input_example = example.split("\n")
    input = process_input(input_example)
    part2 = main_part2(input)
    assert part2 == 3263827


if __name__ == "__main__":

    # test_ex1()

    input_path = "./2025/day6_input.txt"
    input = load_input(input_path)
    input = process_input(input)
    part1 = main_part1(input)
    print(part1)

    part2 = main_part2(input)
    print(part2)
