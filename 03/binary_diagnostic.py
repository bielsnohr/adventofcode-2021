#! /usr/bin/env python3
from pathlib import Path
import math

def gamma_epsilon_product(report: "list[str]") -> int:
    bin_digit_count = sum_bin_digits(report)
    gamma = gamma_rate(bin_digit_count, len(report))
    # epsilon rate is the unsigned complement, but because Python has two's
    # complement representation, this isn't the simple unary bitwise negation
    # (~)
    epsilon = ~gamma & (2**(len(bin(gamma)) - 2) - 1)
    return gamma * epsilon


def gamma_rate(bit_counts: "list[int]", report_length : int) -> int:
    threshold = report_length // 2
    most_common_bit = ['1' if x > threshold else '0' for x in bit_counts]
    bin_string = '0b' + ''.join(most_common_bit)
    return int(bin_string, base=2)


def sum_bin_digits(bin_numbers: "list[str]") -> "list[int]":
    bin_digit_count = [0 for x in range(len(bin_numbers))]
    for bin_num in bin_numbers:
        split_bin = [int(x) for x in bin_num]
        bin_digit_count = [x + y for x, y in zip(split_bin, bin_digit_count)]
    return bin_digit_count


def puzzle_1(inputfile: Path) -> int:
    report = open(inputfile, 'r')
    with open(inputfile, 'r') as file:
        report = [line.rstrip('\n') for line in file]
    return gamma_epsilon_product(report)


def puzzle_2(inputfile: Path) -> int:
    pass


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    #print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
