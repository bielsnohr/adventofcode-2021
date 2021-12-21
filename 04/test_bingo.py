from bingo import BingoBoard, BingoBoardCollection, Path
from bingo import puzzle_1, puzzle_2
import pytest


@pytest.fixture
def bingo_board():
    board_data = [[14, 21, 17, 24, 4],
                  [10, 16, 15, 9, 19],
                  [18, 8, 23, 26, 20],
                  [22, 11, 13, 6, 5],
                  [2, 0, 12, 3, 7]]
    return BingoBoard(board_data=board_data)


@pytest.fixture
def completed_bingo(bingo_board):
    bingo_board.board.mask = [
                        [True, True, True, True, True],
                        [False, False, False, True, False],
                        [False, False, True, False, False],
                        [False, True, False, False, True],
                        [True, True, False, False, True]
                        ]
    bingo_board.last_mark = 24
    return bingo_board


@pytest.fixture
def bingo_board_collection():
    boards_strings = [
        '22 13 17 11  0',
        ' 8  2 23  4 24',
        '21  9 14 16  7',
        ' 6 10  3 18  5',
        ' 1 12 20 15 19',
        '',
        ' 3 15  0  2 22',
        ' 9 18 13 17  5',
        '19  8  7 25 23',
        '20 11 10 24  4',
        '14 21 16 12  6',
        '',
        '14 21 17 24  4',
        '10 16 15  9 19',
        '18  8 23 26 20',
        '22 11 13  6  5',
        ' 2  0 12  3  7'
    ]
    return BingoBoardCollection(boards=boards_strings)


def test_bingoboard_completed_bingo(completed_bingo):
    assert completed_bingo.check_bingo()


def test_bingoboard_mark_value(bingo_board):
    bingo_board.mark_value(24)
    assert (bingo_board.board.mask[0, :] == [False, False, False, True, False]).all()


def test_bingoboard_calculate_score(completed_bingo):
    assert completed_bingo.calculate_score() == 4512


def test_bingoboardcollection_init(bingo_board_collection):
    assert len(bingo_board_collection.boards) == 3
    assert isinstance(bingo_board_collection.boards[0], BingoBoard)


def test_bingoboardcollection_find_winning_score(bingo_board_collection):
    draw = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25,
            12, 22, 18, 20, 8, 19, 3, 26, 1]
    assert bingo_board_collection.find_winning_score(draw=draw) == 4512


def test_bingoboardcollection_find_losing_score(bingo_board_collection):
    draw = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25,
            12, 22, 18, 20, 8, 19, 3, 26, 1]
    assert bingo_board_collection.find_losing_score(draw=draw) == 1924


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 4512


def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 1924
