def load_data(file_path: str) -> list[list[int]]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    reports = []
    for line in lines:
        report = line.split()
        reports.append([int(level) for level in report])

    return reports


def is_safe(report: list[int]) -> bool:

    i = 1
    last = report[0]
    while i < len(report) - 1:
        curr = report[i]
        too_different = abs(curr - last) > 3 or abs(curr - report[i + 1]) > 3
        monotone = last < curr < report[i + 1] or last > curr > report[i + 1]

        if too_different or not monotone:
            return False
        i += 1
        last = curr

    return True


def brute_is_safe_chill(report: list[int]) -> bool:

    if is_safe(report):
        return True

    for i in range(len(report)):
        damped = report.copy()
        damped.pop(i)
        if is_safe(damped):
            return True

    return False


def is_safe_chill(report: list[int]) -> bool:

    if is_safe(report):
        return True

    baddies = set()
    run_diff = []
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        run_diff.append(diff)

        # bad level : 0, change of sign, abs() > 3
        if diff == 0 or abs(diff) > 3:
            baddies.add(i)  # idx of bad level
    run_diff.append(0)

    # check sign change
    pos = sum(1 for d in run_diff if d > 0)
    neg = sum(-1 for d in run_diff if d < 0)
    trend = max(pos, neg, key=abs)

    for i in range(len(run_diff)):
        if trend * run_diff[i] < 0 and i not in baddies:
            baddies.add(i)

    bad = len(baddies)
    if bad == 1:
        bad_idx = baddies.pop()

        sub2 = report.copy()
        sub2.pop(bad_idx)
        if is_safe(sub2):
            return True

        if bad_idx > 0:
            sub1 = report.copy()
            sub1.pop(bad_idx - 1)
            if is_safe(sub1):
                return True

        if bad_idx + 1 < len(report):
            sub3 = report.copy()
            sub3.pop(bad_idx + 1)
            if is_safe(sub3):
                return True

        return False

    return bad == 0


def count_safe_reports(reports: list[list[int]]) -> int:
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def count_safe_reports_chill(reports: list[list[int]]) -> int:
    count = 0
    for report in reports:
        s = str(report)
        if is_safe_chill(report):
            print(f"{s} is Safe")
            count += 1
        else:
            print(f"{s} is Unsafe")
    return count


def part1_ex():
    input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    count = count_safe_reports(input)
    correct = 2
    if count == correct:
        print("Test case passed.")
    else:
        print(f"Got result: {count}")
        print("Something went wrong. Debug your code.")


def part2_ex():
    input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    count = count_safe_reports_chill(input)
    correct = 4
    if count == correct:
        print("Test case passed.")
    else:
        print(f"Got result: {count}")
        print("Something went wrong. Debug your code.")


if __name__ == "__main__":

    part1_ex()
    part2_ex()

    reports = load_data("2024/day2_input.txt")
    total = len(reports)
    count = count_safe_reports(reports)
    print(f"{count} reports out of {total} are safe")

    count = count_safe_reports_chill(reports)
    print(f"{count} reports out of {total} are safe thanks to the dampener")
