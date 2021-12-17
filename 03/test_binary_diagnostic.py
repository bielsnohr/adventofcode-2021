from binary_diagnostic import gamma_epsilon_product, gamma_rate, sum_bin_digits
from binary_diagnostic import puzzle_1, puzzle_2, Path
from binary_diagnostic import valid_reading_functor, filter_readings
from binary_diagnostic import most_common_digit, least_common_digit
from binary_diagnostic import find_unique_rating, life_support_rating
import pytest


@pytest.fixture
def bin_digit_count():
    return [7, 5, 8, 7, 5]


@pytest.fixture
def bin_report():
    return ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
            '11100', '10000', '11001', '00010', '01010']

@pytest.fixture
def int_report(bin_report):
    readings = []
    for reading in bin_report:
        readings.append([int(x) for x in reading])
    return readings


def test_gamma_rate(bin_digit_count):
    assert gamma_rate(bin_digit_count, 12) == 22


def test_sum_bin_digits(bin_report, bin_digit_count):
    assert sum_bin_digits(bin_report) == bin_digit_count


def test_gamma_epsilon_product(bin_report):
    assert gamma_epsilon_product(bin_report) == 198


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 198


@pytest.mark.parametrize(("column", "digit"), [
    [0, 1], [1, 0], [2, 1], [3, 1], [4, 1]
])
def test_valid_reading_functor(column, digit):
    assert valid_reading_functor(column, digit)([1, 0, 1, 1, 1])


def test_filter_readings(int_report):
    filtered_readings = [[1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1],
                         [1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [1, 0, 0, 0, 0],
                         [1, 1, 0, 0, 1]]
    assert filter_readings(int_report, 0, 1) == filtered_readings


def test_common_digit_selectors(int_report):
    assert most_common_digit(report_section=int_report, column=0) == 1
    assert least_common_digit(report_section=int_report, column=0) == 0
    split_report = [[0], [0], [0], [1], [1], [1]]
    assert most_common_digit(report_section=split_report, column=0) == 1
    assert least_common_digit(report_section=split_report, column=0) == 0


def test_find_unique_rating(int_report):
    assert find_unique_rating(report=int_report, column=0, digit_selector=most_common_digit) == [1, 0, 1, 1, 1]
    assert find_unique_rating(report=int_report, column=0, digit_selector=least_common_digit) == [0, 1, 0, 1, 0]


def test_life_support_rating(int_report):
    assert life_support_rating(report=int_report) == 230


def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 230
