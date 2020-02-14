import numpy as np
import string


def count_words(text):
    """Count words in a text.
    Return dictionary of the form {"word": count}
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words, counts = np.unique(text.split(), return_counts=True)
    return dict(zip(words, counts))


def main():
    text = input()
    print(count_words(text))


if __name__ == '__main__':
    main()
