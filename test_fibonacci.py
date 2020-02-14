from fibonacci import fibonacci_to_list


def test_zero():
    assert fibonacci_to_list(0) == []


def test_six():
    assert fibonacci_to_list(5) == [1, 1, 2, 3, 5, 8]
