# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

# """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

# Algorithm
# Define 4 diffs in clockwise movement
# top, right, bottom, left
# Find the position of the guard and determine its orientation (^, >, v, or <).
# Based on the orientation, set the rotating index for the diffs variable
# Also define a set called "visited" which will hold the position of the visited coordinates
# Run a while true loop
# Append the current coordinates to the visited set
# Check the guard's coordinates after adding the diff
# if it's out of bounds, break here
# If it's in bounds, then check if the next character is a boundary
# If it is, flip the guard and update the rotatory index as well

with open("input.txt", "r") as file:
    data = file.read()

    records = data.split("\n")
    grid = [list(row) for row in records]

    ROWS, COLS = len(grid), len(grid[0])

    diffs = [
        (-1, 0),  # top
        (0, 1),  # right
        (1, 0),  # bottom
        (0, -1),  # left
    ]
    possible_guard_orientations = "^>v<"
    rotatory_index = None
    guard_position = None
    # First, find the guard
    for row in range(ROWS):

        for col in range(COLS):

            cur_char = grid[row][col]
            # Found the guard in the grid
            if cur_char in possible_guard_orientations:

                guard_position = (row, col)
                rotatory_index = possible_guard_orientations.index(cur_char)
                break

        # If the guard is found, no need to further iterate other rows
        if guard_position:
            break

    # Next, we start the movement process
    visited = set()
    while True:

        visited.add(guard_position)
        del_row, del_col = diffs[rotatory_index]
        new_row, new_col = guard_position[0] + del_row, guard_position[1] + del_col

        # Check if the guard has went off the grid
        if new_row >= ROWS or new_row < 0 or new_col >= COLS or new_col < 0:
            break

        next_char = grid[new_row][new_col]

        # Check if the next character is a boundary
        if next_char == "#":

            rotatory_index = (rotatory_index + 1) % len(diffs)

        else:

            guard_position = (new_row, new_col)

    # print(visited)
    print(len(visited))
