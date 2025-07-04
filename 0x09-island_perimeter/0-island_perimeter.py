#!/usr/bin/python3
"""Island Perimeter module."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid or not grid[0]:
        return 0

    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                perimeter += 4

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
