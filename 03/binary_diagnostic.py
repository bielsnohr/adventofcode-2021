#! /usr/bin/env python3
from pathlib import Path
from typing import Callable


def gamma_epsilon_product(report: "list[str]") -> int:
    bin_digit_count = sum_bin_digits(report)
    gamma = gamma_rate(bin_digit_count, len(report))
    # epsilon rate is the unsigned complement, but because Python has two's
    # complement representation, this isn't the simple unary bitwise negation
    # (~)
    epsilon = invert_bin_num(gamma)
    return gamma * epsilon


def gamma_rate(bit_counts: "list[int]", report_length: int) -> int:
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


def invert_bin_num(bin_num: int) -> int:
    """Invert a positive binary number (i.e. no consideration of two's complement implementation)

    Args:
        bin_num (int): the binary number

    Returns:
        int: the complement/inverse of bin_num
    """
    return ~bin_num & (2**(len(bin(bin_num)) - 2) - 1)


def bin_list_to_int(bin_list: "list[int]") -> int:
    bin_string = '0b' + ''.join([str(x) for x in bin_list])
    return int(bin_string, base=2)


def filter_readings(report_section: "list[list[int]]", column: int,
                    digit: int) -> "list[list[int]]":
    return list(filter(valid_reading_functor(column, digit), report_section))


def valid_reading_functor(column: int, digit: int) -> Callable:
    def valid_reading(reading: "list[int]") -> bool:
        return reading[column] == digit

    return valid_reading


def most_common_digit(report_section: "list[list[int]]", column: int) -> int:
    sum = 0
    threshold = len(report_section) // 2
    even_length = len(report_section) % 2 == 0
    for reading in report_section:
        sum += reading[column]
    if sum == threshold and even_length:
        most_common_digit = 1
    elif sum > threshold:
        most_common_digit = 1
    else:
        most_common_digit = 0
    return most_common_digit


def least_common_digit(report_section: "list[list[int]]", column: int) -> int:
    return invert_bin_num(most_common_digit(report_section, column))


def find_unique_rating(report: "list[list[int]]", column: int, digit_selector: Callable) -> int:
    digit = digit_selector(report_section=report, column=column)
    report_subsection = filter_readings(report_section=report, column=column, digit=digit)
    if len(report_subsection) == 1:
        return report_subsection[0]
    else:
        return find_unique_rating(report=report_subsection, column=column + 1, digit_selector=digit_selector)


def life_support_rating(report: "list[list[int]]") -> int:
    oxygen_generator_rating = find_unique_rating(report=report, column=0, digit_selector=most_common_digit)
    co2_scrubber_rating = find_unique_rating(report=report, column=0, digit_selector=least_common_digit)
    return bin_list_to_int(oxygen_generator_rating) * bin_list_to_int(co2_scrubber_rating)


def puzzle_1(inputfile: Path) -> int:
    report = open(inputfile, 'r')
    with open(inputfile, 'r') as file:
        report = [line.rstrip('\n') for line in file]
    return gamma_epsilon_product(report)


def puzzle_2(inputfile: Path) -> int:
    report = open(inputfile, 'r')
    with open(inputfile, 'r') as file:
        report = [[int(digit) for digit in line.rstrip('\n')] for line in file]
    return life_support_rating(report)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
