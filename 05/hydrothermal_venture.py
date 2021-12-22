#! /usr/bin/env python3
from pathlib import Path
import numpy as np
import numpy.typing as npt
import re


class VentMap():
    def __init__(self, size: int = 9):
        self.map = np.zeros((size, size), dtype=np.int64)

    def mark_line(self, endpoints: npt.ArrayLike, diagonal: bool = False) -> None:
        """Mark the points that a horizontal or vertical line occupies on the map

        Args:
            endpoints (npt.ArrayLike): A list of the end point coordinates: [x1, y1, x2, y2]
        """
        endpoints = np.asarray(endpoints)
        if endpoints[0] == endpoints[2] or endpoints[1] == endpoints[3]:
            x1, x2 = np.sort(endpoints[[0, 2]])
            y1, y2 = np.sort(endpoints[[1, 3]])
            self.map[y1:y2+1, x1:x2+1] += 1
        elif diagonal:
            x1, x2 = endpoints[[0, 2]]
            y1, y2 = endpoints[[1, 3]]
            dx = np.abs(x2 - x1)
            dy = np.abs(y2 - y1)
            if dx == dy:
                xrange = np.linspace(start=x1, stop=x2, num=dx+1, dtype=np.int64)
                yrange = np.linspace(start=y1, stop=y2, num=dy+1, dtype=np.int64)
                self.map[yrange, xrange] += 1

    def mark_all_lines(self, endpoints_list: npt.ArrayLike, diagonal: bool = False) -> None:
        """Mark the points that a horizontal or vertical line occupies on the map

        Args:
            endpoints (npt.ArrayLike): A list of lists of the end point coordinates: [[x1, y1, x2, y2], [x1, y1, x2, y2], ...]
        """
        for line in endpoints_list:
            self.mark_line(endpoints=line, diagonal=diagonal)

    def calculate_overlap(self):
        return (self.map >= 2).sum()


def puzzle_1(inputfile: Path, diagonal=False) -> int:
    line_parse = re.compile(r'(\d+),(\d+)\s+->\s+(\d+),(\d+)')
    endpoints_list = []
    with open(inputfile, 'r') as file:
        for line in file:
            endpoints_list.append([int(x) for x in line_parse.search(line).groups()])
    endpoints_list = np.array(endpoints_list)
    vent_map = VentMap(size=endpoints_list.max() + 1)
    vent_map.mark_all_lines(endpoints_list, diagonal=diagonal)
    return vent_map.calculate_overlap()


def puzzle_2(inputfile: Path) -> int:
    return puzzle_1(inputfile=inputfile, diagonal=True)


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
