from dive import Submarine, puzzle_1, Path
from dive import AimSubmarine, puzzle_2
import pytest


@pytest.fixture
def submarine():
    return Submarine()


@pytest.fixture
def aimsub():
    return AimSubmarine()


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 150


def test_aimsub_forward(aimsub):
    aimsub.aim = 10
    aimsub.forward(10)
    assert (aimsub.hpos, aimsub.depth) == (10, 100)


def test_aimsub_up_down_forward(aimsub):
    aimsub.down(10)
    aimsub.up(5)
    aimsub.forward(10)
    assert (aimsub.hpos, aimsub.depth) == (10, 50)

def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 900
