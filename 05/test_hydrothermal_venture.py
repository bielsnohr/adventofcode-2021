from numpy.core.fromnumeric import diagonal
from hydrothermal_venture import VentMap, np, Path
from hydrothermal_venture import puzzle_1, puzzle_2
import pytest

line1_mark = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

line2_mark = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])


@pytest.fixture
def list_of_lines():
    return [
        [0, 9, 5, 9],
        [8, 0, 0, 8],
        [9, 4, 3, 4],
        [2, 2, 2, 1],
        [7, 0, 7, 4],
        [6, 4, 2, 0],
        [0, 9, 2, 9],
        [3, 4, 1, 4],
        [0, 0, 8, 8],
        [5, 5, 8, 2]
    ]


@pytest.fixture
def vent_map():
    return VentMap(size=10)


@pytest.fixture
def endstate_map():
    return np.array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]])


@pytest.fixture
def diagonal_mark():
    return ([5, 5, 8, 2],
            np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))


@pytest.fixture
def endstate_diagonal_map():
    return np.array([[1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                     [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
                     [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
                     [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
                     [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
                     [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]])


@pytest.mark.parametrize(("line, line_mark"), [
    ([0, 9, 5, 9], line2_mark), ([2, 2, 2, 1], line1_mark)
])
def test_ventmap_mark_line(vent_map, line, line_mark):
    vent_map.mark_line(endpoints=line)
    assert np.equal(vent_map.map, line_mark).all()


def test_ventmap_mark_all_lines(vent_map, list_of_lines, endstate_map):
    vent_map.mark_all_lines(endpoints_list=list_of_lines)
    assert np.equal(vent_map.map, endstate_map).all()


def test_ventmap_calculate_overlap(vent_map, endstate_map):
    vent_map.map = endstate_map
    assert vent_map.calculate_overlap() == 5


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 5


def test_ventmap_diagonal_mark(vent_map, diagonal_mark):
    endpoints, endstate = diagonal_mark
    vent_map.mark_line(endpoints=endpoints, diagonal=True)
    assert np.equal(vent_map.map, endstate).all()
    

def test_ventmap_diagonal_mark_all_lines(vent_map, list_of_lines, endstate_diagonal_map):
    vent_map.mark_all_lines(endpoints_list=list_of_lines, diagonal=True)
    assert np.equal(vent_map.map, endstate_diagonal_map).all()


def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 12

#
# def test_puzzle_2():
#     assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 1924
