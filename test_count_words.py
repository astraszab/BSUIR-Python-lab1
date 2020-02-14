from count_words import count_words


def test_empty():
    assert count_words('') == {}


def test_hello_world():
    assert count_words('hello world') == {'hello': 1, 'world': 1}


def test_multiple_words():
    assert count_words('hello world hello') == {'hello': 2, 'world': 1}


def test_upper_case():
    assert count_words('Hello world hello') == {'hello': 2, 'world': 1}


def test_punctuation():
    assert count_words('hello, world hello!') == {'hello': 2, 'world': 1}
