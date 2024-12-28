input_data = []


def process_report_original(report):

    # prev diff -> initialize to None
    # curr diff -> also to None
    # check if curr diff is less than 1 or greater than 3
    # return false if condition meets
    # check if prev diff > 0 and curr diff < 0
    # return false if meets and vice versa of condition as well

    prev_diff, cur_diff = None, None
    prev_num = report[0]
    for i in range(1, len(report)):

        cur_num = report[i]
        cur_diff = cur_num - prev_num

        if not prev_diff:
            prev_diff = cur_diff

        if abs(cur_diff) > 3 or abs(cur_diff) < 1:
            return False

        if (prev_diff > 0 and cur_diff < 0) or (prev_diff < 0 and cur_diff > 0):
            return False

        # Update previous values
        prev_diff = cur_diff
        prev_num = cur_num

    return True


def process_report(report):

    # abs(sum) + 1 len(report)
    # return true
    # otherwise
    # try to fix the unsafe report

    diff_arr = []
    prev_num = report[0]
    total_sum = 0
    is_unsafe = False
    for i in range(1, len(report)):

        cur_num = report[i]
        cur_diff = cur_num - prev_num

        if abs(cur_diff) < 0 or abs(cur_diff) > 3:
            is_unsafe = True

        if cur_diff > 0:
            diff_arr.append(1)
        elif cur_diff < 0:
            diff_arr.append(-1)

        # diff_arr.append(cur_diff)

        prev_num = cur_num

    total_sum = sum(diff_arr)
    # Check if report is safe
    # if is_unsafe:
    print(diff_arr, total_sum)
    for i, num in enumerate(diff_arr):

        cur_sum = abs(sum(diff_arr[:i]) + sum(diff_arr[i + 1 :]))
        print(cur_sum)
        # print(diff_arr[:i], diff_arr[i + 1 :], cur_sum)
        if total_sum > 0 and num < 0 or total_sum < 0 and num > 0:

            # Check if the cur_sum is equal to the shortened array
            if cur_sum + 1 == len(report) - 1:
                return True
    if abs(total_sum) + 1 == len(report):
        return True

    # Check if unsafe report can be converted

    return False


with open("input.txt", "r") as file:
    data = file.read()
    all_reports = data.split("\n")

    safe_reports = 0
    for report in all_reports:

        # report = "5 1 2 3 4"
        print("Processing report:", report)
        levels = list(map(int, report.split(" ")))
        is_report_safe = process_report(levels)
        safe_reports += int(is_report_safe)
        # break

    print(safe_reports)
