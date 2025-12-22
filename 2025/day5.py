example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32 """


def load_input(file_path: str) -> list:
    with open(file_path, "r") as f:
        lines = f.readlines()

    return lines


def process_input(input: list) -> tuple:
    for i, line in enumerate(input):
        input[i] = line.strip("\n")
    id_range = input[0]
    idx = 0
    ranges = []
    while id_range != "":
        start, end = id_range.split("-")
        ranges.append((int(start), int(end)))
        idx += 1
        id_range = input[idx]

    idx += 1
    available_ids = []
    while idx < len(input):
        food_id = input[idx]
        available_ids.append(int(food_id))
        idx += 1

    return ranges, available_ids


def main_part1(input: tuple) -> int:
    ranges, available_ids = input

    actual_fresh = 0
    for id in available_ids:
        for r in ranges:
            start, end = r
            if start <= id <= end:
                actual_fresh += 1
                break
    return actual_fresh


def main_part2(input: tuple) -> int:
    ranges, _ = input
    ranges.sort()
    aggr_ranges = [ranges[0]]

    for i, r in enumerate(ranges):
        start, end = r
        if i > 0:
            treated = False
            for j, a in enumerate(aggr_ranges):
                start_a, end_a = a
                if start_a <= start <= end_a and start_a <= end <= end_a:
                    # there is overlap
                    treated = True
                    break
                elif start_a <= start <= end_a and end > end_a:
                    aggr_ranges.pop(j)
                    aggr_ranges.append((start_a, end))
                    treated = True
                    break

            if not treated:
                aggr_ranges.append(r)

    count = 0
    for a in aggr_ranges:
        start, end = a
        count += end - start + 1

    return count


def test_ex1():
    # TODO
    input = process_input(example.split("\n"))
    fresh_count = main_part1(input)
    assert fresh_count == 3


def test_ex2():
    # TODO
    input = process_input(example.split("\n"))
    fresh_count = main_part2(input)
    assert fresh_count == 14


if __name__ == "__main__":

    test_ex1()
    test_ex2()

    input_path = "./2025/day5_input.txt"
    input = load_input(input_path)
    input = process_input(input)
    part1 = main_part1(input)
    print(part1)

    part2 = main_part2(input)
    print(part2)
