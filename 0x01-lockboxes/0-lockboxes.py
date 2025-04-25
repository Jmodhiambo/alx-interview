#!/usr/bin/python3
"""Determines if all the boxes can be opened."""

from typing import List, Set


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Check if all boxes can be opened starting from box 0.

    Each box may contain keys to other boxes. The first box is unlocked.
    A key with the same number as a box opens that box.

    Args:
        boxes (List[List[int]]): A list of lists where each sublist contains
                                 keys (integers) to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        return False

    opened: Set[int] = {0}
    stack: List[int] = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if 0 <= key < len(boxes) and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
