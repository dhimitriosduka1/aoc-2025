import os
import copy


def solve_part1():
    with open(os.path.join(os.path.dirname(__file__), "input_part1.txt")) as f:
        raw_lines = f.read().strip().splitlines()

    rows = len(raw_lines)
    cols = len(raw_lines[0])

    grid = ["." * (cols + 2)]
    for line in raw_lines:
        grid.append(f".{line}.")
    grid.append("." * (cols + 2))

    count_result = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if grid[r][c] == ".":
                continue

            neighbors = 0
            for dr, dc in directions:
                if grid[r + dr][c + dc] == "@":
                    neighbors += 1

            if neighbors < 4:
                count_result += 1

    print(f"Part 1 results: {count_result}")


def solve_part2():
    with open(os.path.join(os.path.dirname(__file__), "input_part2.txt")) as f:
        raw_lines = f.read().strip().splitlines()

    rows = len(raw_lines)
    cols = len(raw_lines[0])

    grid = ["." * (cols + 2)]
    for line in raw_lines:
        grid.append(f".{line}.")
    grid.append("." * (cols + 2))

    count_result = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while True:
        iteration_count = 0
        temp_grid = copy.deepcopy(grid)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if grid[r][c] == ".":
                    continue

                neighbors = 0
                for dr, dc in directions:
                    if grid[r + dr][c + dc] == "@":
                        neighbors += 1

                if neighbors < 4:
                    iteration_count += 1
                    temp_grid[r] = temp_grid[r][:c] + "." + temp_grid[r][c + 1 :]

        if iteration_count == 0:
            break

        count_result += iteration_count

        grid = temp_grid

    print(f"Part 2 results: {count_result}")


solve_part1()
solve_part2()
