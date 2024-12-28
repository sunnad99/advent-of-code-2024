with open("input.txt", "r") as file:
    data = file.read()

    #     data = """MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX
    #     """

    grid = [list(line) for line in data.split("\n")[:-1]]

    # If the character starts with an "X", explore it
    # otherwise skip it
    # When exploring an X, check the following 8 directions
    # Up,
    # top right,
    # right,
    # bottom right,
    # bottom,
    # bottom left,
    # left, and
    # top left
    # for every direction
    # check if its the edge of the grid
    # then check if the length is met or if word is XMAS
    # return true
    # otherwise
    # return false

    # if its not the edge, check the length
    # if equal to 4
    # and word is XMAS
    # return true
    # is not
    # return false

    # NOTES:
    # Lets pass the direction as well so we keep iterating in that direction
    # If a direction is not given, iterate in all directions
    ROWS, COLS = len(grid), len(grid[0])

    # PART 1
    directions = {
        "top": (-1, 0),
        "top_right": (-1, 1),
        "right": (0, 1),
        "bottom_right": (1, 1),
        "bottom": (1, 0),
        "bottom_left": (1, -1),
        "left": (0, -1),
        "top_left": (-1, -1),
    }

    def dfs(row, col, dir_, word):

        # If row and col are out of bounds
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:

            if len(word) == 4 and word == "XMAS":
                return 1
            else:
                return 0

        # If the length of the word is 4 and the word is XMAS
        if len(word) == 4:

            if word == "XMAS":
                return 1

            else:
                return 0

        result = 0
        word += grid[row][col]
        if dir_:

            l, r = directions[dir_]
            new_coord = (row + l, col + r)
            result += dfs(*(new_coord), dir_, word)
        else:

            for new_dir, delta in directions.items():
                del_l, del_r = delta
                new_coord = (row + del_l, col + del_r)
                result += dfs(*(new_coord), new_dir, word)

        return result

    total_nums = 0
    for row in range(ROWS):

        for col in range(COLS):

            total_nums += dfs(row, col, None, "")

    print(total_nums)

    # PART 2

    back_slash = [
        (-1, -1),  # top left
        (1, 1),  # bottom right
    ]

    forward_slash = [
        (-1, 1),  # top right
        (1, -1),  # bottom left
    ]

    total_cross_mas = 0
    for row in range(1, ROWS - 1):

        for col in range(1, COLS - 1):

            char = grid[row][col]

            if char == "A":

                back_word, forward_word = char, char
                for del_l, del_r in back_slash:
                    back_word += grid[row + del_l][col + del_r]

                for del_l, del_r in forward_slash:
                    forward_word += grid[row + del_l][col + del_r]

                # print(row, col)
                # print(back_word, forward_word)

                mas_word = set("MAS")
                if (
                    len(mas_word.intersection(set(back_word))) == 3
                    and len(mas_word.intersection(set(forward_word))) == 3
                ):
                    if set(forward_word) == set(back_word):
                        total_cross_mas += 1

    print(total_cross_mas)
