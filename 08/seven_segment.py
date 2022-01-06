#! /usr/bin/env python3
from os import read
from pathlib import Path
from typing import Callable, Dict, Tuple
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


def decode_entry(reading: "list[str]") -> "dict[str, str]":
    """Decode the signals to identify digits for an entry

    Args:
        readings (list[str]): list of signals from the 4 digit displays. These
                              are the un-decoded segment signals acquired from observation.

    Returns:
        dict[str, int]: A dictionary mapping the (sorted) segment signals to their digits
    """
    unique_signal_length_map = {2: 1, 3: 7, 4: 4, 7: 8}
    five_segments = []
    six_segments = []
    segment_map = {}
    set_map = {}

    for signal in reading:
        sig_len = len(signal)
        if sig_len in unique_signal_length_map.keys():
            segment_map[''.join(sorted(signal))] = str(unique_signal_length_map[sig_len])
            set_map[unique_signal_length_map[sig_len]] = set(signal)
        elif sig_len == 5:
            five_segments.append(set(signal))
        elif sig_len == 6:
            six_segments.append(set(signal))

    for signal in six_segments:
        if len(set_map[1] - signal) == 1:
            segment_map[''.join(sorted(signal))] = '6'
            set_map[6] = signal
        elif len(set_map[4] - signal) == 0:
            segment_map[''.join(sorted(signal))] = '9'
        else:
            segment_map[''.join(sorted(signal))] = '0'

    for signal in five_segments:
        if len(set_map[6] - signal) == 1:
            segment_map[''.join(sorted(signal))] = '5'
            five_segments.remove(signal)
            set_map[5] = signal
            break

    for signal in five_segments:
        if len(signal - set_map[5]) == 1:
            segment_map[''.join(sorted(signal))] = '3'
        else:
            segment_map[''.join(sorted(signal))] = '2'

    return segment_map


def sum_decoded_outputs(readings: "list[list[list[str]]]") -> int:
    output_sum = 0
    for reading in readings:
        signal_map = decode_entry(reading=reading[0])
        number = ''
        for output in reading[1]:
            number += signal_map[''.join(sorted(output))]
        output_sum += int(number)
    return output_sum


def puzzle_1(inputfile: Path) -> int:
    readings = []
    with open(inputfile, 'r') as file:
        for line in file:
            signals, reading = line.split(sep='|')
            readings.append([signals.split(), reading.split()])
    return count_unique_segment_digits(readings=readings)


def puzzle_2(inputfile: Path) -> int:
    readings = []
    with open(inputfile, 'r') as file:
        for line in file:
            signals, reading = line.split(sep='|')
            readings.append([signals.split(), reading.split()])
    return sum_decoded_outputs(readings=readings)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
