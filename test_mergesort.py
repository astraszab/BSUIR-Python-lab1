from mergesort import mergesort


def test_empty():
    assert mergesort('') == []


def test_simple_array():
    assert mergesort('12 0 3 2 8') == [0, 2, 3, 8, 12]
