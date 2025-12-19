example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def load_input(file_path: str) -> str:
    with open(file_path, "r") as f:
        line = f.readline()
    return line


def process_input(raw_input: str) -> list[tuple]:
    ranges = raw_input.split(",")
    start_end_tuple = []
    for range in ranges:
        start, end = range.split("-")
        int_start = int(start)
        int_end_exclusive = int(end) + 1
        start_end_tuple.append((int_start, int_end_exclusive))

    return start_end_tuple


def sum_invalid_id(input: str) -> int:

    ranges = process_input(input)
    sum_invalid = 0
    for start, end in ranges:
        # look for invalid ID
        for id in range(start, end):
            str_id = str(id)
            n = len(str_id)
            if str_id[: n // 2] == str_id[n // 2 :]:
                # invalid
                sum_invalid += id

    return sum_invalid


def sum_invalid_id_new(input: str) -> int:
    ranges = process_input(input)
    sum_invalid = 0
    for start, end in ranges:
        # look for invalid ID
        for id in range(start, end):
            if invalid(id):
                sum_invalid += id

    return sum_invalid


def invalid(id: int) -> bool:
    str_id = str(id)
    n = len(str_id)
    if n == 1:
        return False
    if str_id[: n // 2] == str_id[n // 2 :]:
        return True
    if len(set([c for c in str_id])) == 1:
        return True

    for sub_length in range(1, n // 2):
        if n % sub_length == 0:
            separate_sub_seq = [
                str_id[i : i + sub_length] for i in range(0, n, sub_length)
            ]
            sequences = set(separate_sub_seq)
            if len(sequences) == 1:
                return True

    return False


def test_ex1():
    assert sum_invalid_id(example) == 1227775554


def test_ex2():
    assert sum_invalid_id_new(example) == 4174379265


def test_invalid_one_digit():
    assert not invalid(1)


def test_invalid_two_digit():
    assert invalid(11)


def test_valid_two_digit():
    assert not invalid(12)


# print(process_input(example))

if __name__ == "__main__":
    input_file = "./2025/day2_input.txt"
    input = load_input(input_file)
    print(sum_invalid_id_new(input))
