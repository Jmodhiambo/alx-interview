#!/usr/bin/python3
"""Solves the N Queens problem using backtracking."""

import sys


def is_safe(row, col, solution):
    """
    Check if placing a queen at (row, col) is safe.
    It must not share the same column or diagonal with any other queen.
    """
    for r, c in solution:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, solution=[]):
    """
    Recursively tries to place queens row by row.
    If a valid solution is found, it is printed.
    """
    if row == n:
        # All queens are placed successfully
        print(solution)
        return

    for col in range(n):
        if is_safe(row, col, solution):
            # Try placing queen at (row, col) and move to next row
            solve_nqueens(n, row + 1, solution + [[row, col]])


def main():
    """Main entry point: validate arguments and start the solver."""

    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try converting the argument to an integer
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure board is at least 4x4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Start solving the N queens problem
    solve_nqueens(n)


if __name__ == "__main__":
    main()
