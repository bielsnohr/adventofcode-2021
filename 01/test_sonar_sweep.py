from sonar_sweep import count_sweep_increases, puzzle_1, Path
from sonar_sweep import count_window_increases
import pytest


@pytest.fixture
def input_report():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_count_sweep_increases(input_report):
    assert count_sweep_increases(input_report) == 7


def test_count_window_increases(input_report):
    assert count_window_increases(input_report) == 5


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 7
