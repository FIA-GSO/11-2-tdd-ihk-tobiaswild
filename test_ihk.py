import pytest

from ihk import *

testdata_prozent = [
    (0, 100, 0),
    (50, 100, 50),
    (100, 100, 100),
    (-1, 100, ValueError),
    (101, 100, ValueError),
    (0, 6, 0),
    (0, 5, ValueError),
    ("0", 100, TypeError),
    (0, "100", TypeError),
]


@pytest.mark.parametrize("value, max_value, expected_value", testdata_prozent)
def test_prozent_berechnen__v0(value: int, max_value: int, expected_value):
    result = prozent_berechnen(value, max_value)

    if type(expected_value) is not float:
        with pytest.raises(expected_value):
            assert True

    assert result == expected_value


testdata_note = [
    (100, "sehr gut"),
    (92, "sehr gut"),
    (91, "gut"),
    (81, "gut"),
    (80, "befriedigend"),
    (67, "befriedigend"),
    (66, "ausreichend"),
    (50, "ausreichend"),
    (49, "mangelhaft"),
    (30, "mangelhaft"),
    (29, "ungenügend"),
    (0, "ungenügend"),
    (-1, ValueError),
    (101, ValueError),
    ("0", TypeError),
]


@pytest.mark.parametrize("value, expected_value", testdata_note)
def test_note_berechnen__v0(value: int, expected_value):
    result = note_berechnen(value)

    if type(expected_value) is not float:
        with pytest.raises(expected_value):
            assert True

    assert result == expected_value
