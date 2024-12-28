with open("input.txt", "r") as file:
    data = file.read()

    #     data = """47|53
    # 97|13
    # 97|61
    # 97|47
    # 75|29
    # 61|13
    # 75|53
    # 29|13
    # 97|29
    # 53|29
    # 61|53
    # 97|53
    # 61|29
    # 47|13
    # 75|47
    # 97|75
    # 47|61
    # 75|61
    # 47|29
    # 75|13
    # 53|13

    # 75,47,61,53,29
    # 97,61,53,29,13
    # 75,29,13
    # 75,97,47,61,53
    # 61,13,29
    # 97,13,75,29,47
    # """

    rules, updates = data.split("\n\n")

    # PART 1
    adj_list = {}
    for rule in rules.split("\n"):

        prev_node, next_node = list(map(int, rule.split("|")))

        if prev_node not in adj_list:
            adj_list[prev_node] = []

        adj_list[prev_node].append(next_node)

    # print(adj_list)
    total_sum = 0
    for update in updates.split("\n")[:-1]:

        nums = list(map(int, update.split(",")))
        visited = set()
        is_wrong = False
        for num in nums:

            for visited_num in visited:

                greater_nums = adj_list.get(num)

                # If no rule exists, continue
                if not greater_nums:
                    continue
                # print(visited_num, num, greater_nums)

                # If the already visited numbers are found in the adj_list, then the rule has broken
                if visited_num in greater_nums:
                    is_wrong = True
                    break

            visited.add(num)

            # Don't iterate any further if even a single rule breaks
            if is_wrong:
                break

        # If its a correct update, identify the middle number
        mid_num = 0
        if not is_wrong:
            # print(update)
            size = len(nums)
            if size % 2 == 0:

                l, r = (size // 2) - 1, (size // 2)
                mid_num = (nums[l] + nums[r]) / 2
            else:
                mid_num = nums[size // 2]

        total_sum += mid_num

    print(total_sum)
