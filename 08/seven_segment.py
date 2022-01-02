#! /usr/bin/env python3
from os import read
from pathlib import Path
from typing import Callable, Tuple
import numpy.typing as npt
import numpy as np


def count_unique_segment_digits(readings: "list[list[list[str]]]") -> int:
    """Count the digits formed by unique display segments in the display output for an entry

    Args:
        readings (list[list[list[str]]]): list of readings of the 4 digit displays. Each reading contains two lists,
                 the first being the observations of the unique signals, the second being the 4 digits of the output.

    Returns:
        int: The count of digits in the output that are formed by unique segment combinations (i.e. 1, 4, 7, 8)
    """
    count = 0
    for reading in readings:
        for digit in reading[1]:
            if len(digit) in (2, 3, 4, 7):
                count += 1

    return count

def puzzle_1(inputfile: Path) -> int:
    readings = []
    with open(inputfile, 'r') as file:
        for line in file:
            signals, reading = line.split(sep='|')
            readings.append([signals.split(), reading.split()])
    return count_unique_segment_digits(readings=readings)


def puzzle_2(inputfile: Path) -> int:
    pass
    # with open(inputfile, 'r') as file:
    #     crab_positions = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    # return minimise_fuel_cost(crab_positions=crab_positions, distance_function=arithmetic_sum)[0]


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
