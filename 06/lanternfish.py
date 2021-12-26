#! /usr/bin/env python3
from pathlib import Path
from copy import deepcopy

########################################
# Naive approach (not correct!!!)
########################################

def increment_day(lanternfish_timers: "list[int]", regular_cycle: int = 6, new_cycle: int = 8) -> "list[int]":
    """Increment the day for a group of reproducing lantern fish

    Args:
        lanternfish_timers (list[int]): The current reproductive countdown timers for the lantern fish.
        regular_cycle (int, optional): The normal countdown timer for a lantern fish. Defaults to 6.
        new_cycle (int, optional): The initial countdown timer for a lantern fish that has just been born. Defaults to
                                   8.

    Returns:
        list[int]: The new list of lantern fish countdown timers after incrementing the day.
    """
    new_timers = deepcopy(lanternfish_timers)
    for i, timer in enumerate(lanternfish_timers):
        if timer == 0:
            new_timers[i] = regular_cycle
            new_timers.append(new_cycle)
        else:
            new_timers[i] -= 1

    return new_timers


def simulate_lanternfish_growth(initial_timer_state: "list[int]", simulation_days: int, regular_cycle: int = 6,
                                new_cycle: int = 8) -> int:
    """Simulate the lanternfish over a given number of days and determine the final population size.

    Args:
        initial_timer_state (list[int]): The initial reproductive countdown timers for the lantern fish.
        simulation_days (int): The number of days to run the simulation
        regular_cycle (int, optional): The normal countdown timer for a lantern fish. Defaults to 6.
        new_cycle (int, optional): The initial countdown timer for a lantern fish that has just been born. Defaults to
                                   8.

    Returns:
        int: The number of lantern fish at the end of the simulation.
    """
    lanternfish_timers = initial_timer_state
    for i in range(simulation_days):
        lanternfish_timers = increment_day(lanternfish_timers=lanternfish_timers, regular_cycle=regular_cycle,
                                           new_cycle=new_cycle)
    return len(lanternfish_timers)


########################################
# Correct approach
########################################
class LanternfishTracker():
    def __init__(self, timer_list: "list[int]"):
        self.timers = [0 for x in range(9)]
        for time in timer_list:
            self.timers[time] += 1

    def increment_day(self) -> None:
        lanternfish = self.timers.pop(0)
        self.timers[6] += lanternfish
        self.timers.append(lanternfish)

    def simulate_growth(self, days: int) -> int:
        [self.increment_day() for i in range(days)]
        return sum(self.timers)


def puzzle_1(inputfile: Path, diagonal=False) -> int:
    with open(inputfile, 'r') as file:
        initial_state = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    return simulate_lanternfish_growth(initial_timer_state=initial_state, simulation_days=80)


def puzzle_2(inputfile: Path) -> int:
    with open(inputfile, 'r') as file:
        initial_state = [int(x) for x in file.readline().strip('\n').split(sep=',')]
    tracker = LanternfishTracker(timer_list=initial_state)
    return tracker.simulate_growth(days=256)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
