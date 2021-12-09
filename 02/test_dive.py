from dive import Submarine, puzzle_1, Path
import pytest


@pytest.fixture
def submarine():
    return Submarine()


def test_puzzle_1(submarine):
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 150
