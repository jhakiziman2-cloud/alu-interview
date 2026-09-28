#!/usr/bin/python3
"""
0-rain module

Contains a function that calculates the total amount of rainwater
that can be retained given a list of non-negative integers
representing wall heights of unit width 1.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained
    after it rains, given a list of wall heights.

    Args:
        walls (list): A list of non-negative integers representing
            the heights of walls with unit width 1.

    Returns:
        int: The total amount of rainwater retained. Returns 0 if
            the list is empty.
    """
    if not walls:
        return 0

    length = len(walls)
    left_max = [0] * length
    right_max = [0] * length

    left_max[0] = walls[0]
    for i in range(1, length):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[length - 1] = walls[length - 1]
    for i in range(length - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(length):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water
