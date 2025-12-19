def load_input_rotation(file: str) -> list:
    with open(file, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line[:-1]
    return lines


def rotate(code: int, rotation: str) -> tuple:
    direction = rotation[0]
    amount = int(rotation[1:])

    mapping = {"L": -1, "R": 1}
    amount *= mapping[direction]

    code = (code + amount) % 100
    return code, amount


def rotation_code(n: int, rotations: list) -> int:
    code = n  # start of the lock
    real_code = 0
    for rotation in rotations:
        code, _ = rotate(code, rotation)

        if code == 0:
            real_code += 1

    return real_code


def new_rotation_naive(n: int, rotations: list) -> int:
    code = n  # start of the lock
    real_code = 0
    for rotation in rotations:

        new_code, amount = rotate(code, rotation)  # amount is signed
        for _ in range(abs(amount)):
            if amount < 0:
                code = (code - 1) % 100
            else:
                code = (code + 1) % 100
            if code == 0:
                real_code += 1
        code = new_code
    return real_code


# print(load_input_rotation("2025/day1_input.txt"))

input_file = "2025/day1_input.txt"
input = load_input_rotation(input_file)

print(rotation_code(50, input))
print(new_rotation_naive(50, input))


## TESTS


def test_example_part1():
    input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    code = rotation_code(50, input)

    assert code == 3


def test_example_new_naive():
    input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    code = new_rotation_naive(50, input)

    assert code == 6
