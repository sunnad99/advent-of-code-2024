with open("input.txt", "r") as file:
    data = file.read()

    sub_str = []
    total_sum = 0
    stack = []
    for i, char in enumerate(data):

        if char in "mul(,)" or char.isnumeric():
            stack.append(char)

        if char == ")":

            while stack:
                cur_char = stack.pop()
                sub_str.insert(0, cur_char)

            final_str = "".join(sub_str)
            if (
                "mul" in final_str
                and final_str.count("(") == 1
                and final_str.count(")") == 1
                and final_str.count(",") == 1
            ):
                print(final_str)
                left, right = final_str.split(",")
                total_sum += int(left[4:]) * int(right[:-1])

            sub_str = []

        if char == "m" and "m" in stack:
            stack = ["m"]

    print(total_sum)
