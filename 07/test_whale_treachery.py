from whale_treachery import calculate_fuel
from whale_treachery import puzzle_1, puzzle_2, Path
import pytest


@pytest.fixture
def crab_positions():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_calculate_fuel(crab_positions):
    assert calculate_fuel(crab_positions=crab_positions) == 37


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 37

# def test_puzzle_2():
#     assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 26984457539
