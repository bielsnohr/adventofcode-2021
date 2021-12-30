#! /usr/bin/env python3
from pathlib import Path
from typing import Callable, Tuple
import numpy.typing as npt
import numpy as np
import scipy.optimize as opt


def calculate_fuel(crab_positions: npt.ArrayLike) -> int:
    positions = np.asarray(crab_positions)
    median = np.floor(np.median(positions))
    return np.sum(np.abs(positions - median))


def fuel_cost(position: int, crab_positions: npt.ArrayLike, distance_function: Callable) -> int:
    positions = np.asarray(crab_positions)
    dist_func = np.vectorize(distance_function, otypes=[np.int64])
    return np.sum(dist_func(positions, position))


def abs_diff(a, b):
    return np.int64(np.abs(a - b))


def arithmetic_sum(a, b):
    n = np.abs(a - b)
    return np.int64(n * (n + 1) / 2)


def minimise_fuel_cost(crab_positions: npt.ArrayLike, distance_function: Callable) -> Tuple[int, int]:
    def f(position):
        return fuel_cost(position, crab_positions, distance_function)
    positions = np.asarray(crab_positions)
    mid = np.floor(np.median(positions))
    costs = [f(mid-1), f(mid), f(mid+1)]
    while True:
        if costs[1] < costs[0] and costs[1] < costs[2]:
            return (costs[1], mid)
        elif costs[0] < costs[1]:
            mid -= 1
            costs.pop()
            costs.insert(0, f(mid-1))
        elif costs[2] < costs[1]:
            mid += 1
            costs.pop(0)
            costs.append(f(mid+1))


def puzzle_1(inputfile: Path, diagonal=False) -> int:
    with open(inputfile, 'r') as file:
        crab_positions = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    return calculate_fuel(crab_positions=crab_positions)


def puzzle_2(inputfile: Path) -> int:
    with open(inputfile, 'r') as file:
        crab_positions = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    return minimise_fuel_cost(crab_positions=crab_positions, distance_function=arithmetic_sum)[0]


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
