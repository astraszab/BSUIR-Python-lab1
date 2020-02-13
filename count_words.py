import numpy as np


def count_words(text):
    """Count words in a text.
    Return dictionary of the form {"word": count}
    """
    words, counts = np.unique(text.split(), return_counts=True)
    return dict(zip(words, counts))


def main():
    text = input()
    print(count_words(text))


if __name__ == '__main__':
    main()
