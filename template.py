example = ""


def load_input(file_path: str):
    with open(file_path, "r") as f:
        lines = f.readlines()
    # TODO


def process_input(input):
    # modify if necessary
    return input


# TODO : write the main function
def main_part1(input) -> int:
    return 0


def main_part2(input) -> int:
    return 0


def test_ex1():
    # TODO
    assert True


def test_ex2():
    # TODO
    assert True


if __name__ == "__main__":

    # test_ex1()

    input_path = "./YYYY/dayN_input.txt"
    input = load_input(input_path)
    input = process_input(input)
    part1 = main_part1(input)
    print(part1)

    part2 = main_part2(input)
    print(part2)
