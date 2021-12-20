#! /usr/bin/env python3
from pathlib import Path
from typing import Iterable
import numpy as np
import numpy.typing as npt


class BingoBoard():
    def __init__(self, board_data: npt.ArrayLike):
        self.last_mark = None
        if board_data is not None:
            self.board = np.ma.masked_array(data=board_data)

    def check_bingo(self):
        return np.any([self.board.mask.all(axis=x) for x in range(2)])

    def mark_value(self, value):
        self.board.mask = self.board.mask | (self.board.data == value)
        self.last_mark = value

    def calculate_score(self):
        return self.board.sum() * self.last_mark


class BingoBoardCollection():
    def __init__(self, boards: "list[str]") -> None:
        temp_board = []
        self.boards = []
        for line in boards:
            if line == '':
                self.boards.append(BingoBoard(board_data=temp_board))
                temp_board = []
            else:
                temp_board.append([int(x) for x in line.split()])
        else:
            self.boards.append(BingoBoard(board_data=temp_board))

    def find_winning_score(self, draw: "list[int]") -> int:
        for value in draw:
            for board in self.boards:
                board.mark_value(value)
                if board.check_bingo():
                    return board.calculate_score()
        else:
            raise RuntimeError("No winning board found.")


def puzzle_1(inputfile: Path) -> int:
    with open(inputfile, 'r') as file:
        draw = [int(x) for x in file.readline().strip('\n').split(',')]
        file.readline()
        board_strings = []
        for line in file:
            board_strings.append(line.strip('\n'))
    bingo_boards = BingoBoardCollection(boards=board_strings)
    return bingo_boards.find_winning_score(draw=draw)


def puzzle_2(inputfile: Path) -> int:
    pass


def main():
    inputfile = Path("puzzle_1_input.txt")
    print(f"Puzzle 1 Answer = {puzzle_1(inputfile)}")
    # print(f"Puzzle 2 Answer = {puzzle_2(inputfile)}")


if __name__ == "__main__":
    main()
