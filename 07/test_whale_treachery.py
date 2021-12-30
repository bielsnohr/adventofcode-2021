from whale_treachery import calculate_fuel, abs_diff, fuel_cost, arithmetic_sum, minimise_fuel_cost
from whale_treachery import puzzle_1, puzzle_2, Path
import pytest


@pytest.fixture
def crab_positions():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_calculate_fuel(crab_positions):
    assert calculate_fuel(crab_positions=crab_positions) == 37


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 37


def test_fuel_cost(crab_positions):
    assert fuel_cost(2, crab_positions, abs_diff) == 37
    assert fuel_cost(5, crab_positions, arithmetic_sum) == 168


def test_arithmetic_sum():
    assert arithmetic_sum(16, 5) == 66


def test_minimise_fuel_cost(crab_positions):
    assert minimise_fuel_cost(crab_positions, abs_diff) == (37, 2)
    assert minimise_fuel_cost(crab_positions, arithmetic_sum) == (168, 5)

# def test_puzzle_2():
#     assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 26984457539
