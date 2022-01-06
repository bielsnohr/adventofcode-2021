from seven_segment import count_unique_segment_digits, decode_entry, sum_decoded_outputs
from seven_segment import puzzle_1, puzzle_2, Path
import pytest


@pytest.fixture
def signals():
    return [
        [['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'],
         ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
        [['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'],
         ['fcgedb', 'cgb', 'dgebacf', 'gc']],
        [['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'],
         ['cg', 'cg', 'fdcagb', 'cbg']],
        [['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'],
         ['efabcd', 'cedba', 'gadfec', 'cb']],
        [['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'],
         ['gecf', 'egdcabf', 'bgf', 'bfgea']],
        [['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'],
         ['gebdcfa', 'ecba', 'ca', 'fadegcb']],
        [['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'],
         ['cefg', 'dcbef', 'fcge', 'gbcadfe']],
        [['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'],
         ['ed', 'bcgafe', 'cdgba', 'cbgef']],
        [['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'],
         ['gbdfcae', 'bgc', 'cg', 'cgb']],
        [['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'],
         ['fgae', 'cfgab', 'fg', 'bagce']]
    ]


@pytest.fixture
def hard_signal():
    return (['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
            {'abcdefg': '8', 'bcdef': '5', 'acdfg': '2', 'abcdf': '3', 'abd': '7', 'abcdef': '9', 'bcdefg': '6', 'abef': '4',
             'abcdeg': '0', 'ab': '1'})


def test_count_unique_segment_digits(signals):
    assert count_unique_segment_digits(readings=signals) == 26


def test_puzzle_1():
    assert puzzle_1(Path(__file__).parent / "puzzle_1_test_input.txt") == 26


def test_decode_entry(hard_signal):
    decoded_signals = decode_entry(reading=hard_signal[0])
    for key in decoded_signals:
        assert decoded_signals[key] == hard_signal[1][key]


def test_sum_decoded_outputs(signals):
    assert sum_decoded_outputs(readings=signals) == 61229


def test_puzzle_2():
    assert puzzle_2(Path(__file__).parent / "puzzle_1_test_input.txt") == 61229
