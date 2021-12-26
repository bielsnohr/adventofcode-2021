from lanternfish import increment_day, simulate_lanternfish_growth, LanternfishTracker
from lanternfish import puzzle_1, puzzle_2, Path
import pytest


@pytest.fixture
def initial_state():
    return [3, 4, 3, 1, 2]


@pytest.fixture
def lanternfish_tracker(initial_state):
    return LanternfishTracker(timer_list=initial_state)


def test_increment_day(initial_state):
    day_1_state = [2, 3, 2, 0, 1]
    day_2_state = [1, 2, 1, 6, 0, 8]
    assert increment_day(lanternfish_timers=initial_state) == day_1_state
    assert increment_day(lanternfish_timers=day_1_state) == day_2_state


def test_simulate_lanternfish_growth(initial_state):
    assert simulate_lanternfish_growth(initial_timer_state=initial_state, simulation_days=80) == 5934


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 5934


def test_long_simulation(lanternfish_tracker):
    assert lanternfish_tracker.simulate_growth(days=256) == 26984457539


def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 26984457539
