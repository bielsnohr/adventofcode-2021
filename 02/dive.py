#! /usr/bin/env python3
from pathlib import Path


class Submarine():
    def __init__(self):
        self.hpos, self.depth = (0, 0)

    def forward(self, units):
        self.hpos += units

    def up(self, units):
        self.depth -= units

    def down(self, units):
        self.depth += units

    def execute_instruction(self, instruction, units):
        self.__getattribute__(instruction)(units)

    def multiply_positions(self):
        return self.hpos * self.depth


class AimSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, units):
        self.hpos += units
        self.depth += self.aim * units

    def up(self, units):
        self.aim -= units

    def down(self, units):
        self.aim += units


def puzzle_1(inputfile: Path) -> int:
    aoc_sub = Submarine()
    with open(inputfile, 'r') as file:
        for line in file:
            instruction, units = line.split()
            aoc_sub.execute_instruction(instruction, int(units))
    return aoc_sub.multiply_positions()


def puzzle_2(inputfile: Path) -> int:
    aoc_sub = AimSubmarine()
    with open(inputfile, 'r') as file:
        for line in file:
            instruction, units = line.split()
            aoc_sub.execute_instruction(instruction, int(units))
    return aoc_sub.multiply_positions()


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
