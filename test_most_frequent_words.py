from most_frequent_words import most_frequent_words
import string


def test_empty():
    assert most_frequent_words('') == ''


def test_less_than_ten_words():
    assert most_frequent_words('Hello, world hello') == 'hello world'


def test_more_than_ten_words():
    letters = string.ascii_lowercase
    text = ''
    for count, letter in enumerate(letters):
        text += f'{letter} ' * count
    assert most_frequent_words(text) == 'z y x w v u t s r q'
