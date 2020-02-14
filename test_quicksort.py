from quicksort import quicksort


def test_empty():
    assert quicksort('') == []


def test_simple_array():
    assert quicksort('12 0 3 2 8') == [0, 2, 3, 8, 12]
