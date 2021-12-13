from binary_diagnostic import gamma_epsilon_product, gamma_rate, sum_bin_digits
from binary_diagnostic import puzzle_1, Path
import pytest


@pytest.fixture
def bin_digit_count():
    return [7, 5, 8, 7, 5]


@pytest.fixture
def bin_report():
    return ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
            '11100', '10000', '11001', '00010', '01010']


def test_gamma_rate(bin_digit_count):
    assert gamma_rate(bin_digit_count, 12) == 22


def test_sum_bin_digits(bin_report, bin_digit_count):
    assert sum_bin_digits(bin_report) == bin_digit_count

def test_gamma_epsilon_product(bin_report):
    assert gamma_epsilon_product(bin_report) == 198


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 198
