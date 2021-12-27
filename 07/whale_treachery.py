#! /usr/bin/env python3
from pathlib import Path
import numpy.typing as npt
import numpy as np


def calculate_median(crab_positions: npt.ArrayLike) -> int:
    return np.floor(np.median(crab_positions))


def calculate_fuel(crab_positions: npt.ArrayLike) -> int:
    positions = np.asarray(crab_positions)
    median = np.floor(np.median(positions))
    return np.sum(np.abs(positions - median))


def puzzle_1(inputfile: Path, diagonal=False) -> int:
    with open(inputfile, 'r') as file:
        crab_positions = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    return calculate_fuel(crab_positions=crab_positions)


def puzzle_2(inputfile: Path) -> int:
    pass
    # with open(inputfile, 'r') as file:
    #     initial_state = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    # tracker = LanternfishTracker(timer_list=initial_state)
    # return tracker.simulate_growth(days=256)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    #print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
