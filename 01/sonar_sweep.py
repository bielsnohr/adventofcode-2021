#! /usr/bin/env python3
from pathlib import Path


def count_sweep_increases(report: "list[int]") -> int:
    prev = report[0]
    count = 0
    for i in report:
        if i > prev:
            count += 1
        prev = i

    return count


def count_window_increases(report: "list[int]") -> int:
    prev = sum(report[:3])
    count = 0
    for i in range(len(report)-2):
        current = sum(report[i:i+3])
        if current > prev:
            count += 1
        prev = current
    return count


def puzzle_1(inputfile: Path) -> int:
    report = []
    with open(inputfile, 'r') as file:
        for line in file:
            report.append(int(line))
    return count_sweep_increases(report)


def puzzle_2(inputfile: Path) -> int:
    report = []
    with open(inputfile, 'r') as file:
        for line in file:
            report.append(int(line))
    return count_window_increases(report)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
