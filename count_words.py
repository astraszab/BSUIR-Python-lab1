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
    input_filename = 'input_files/input_for_count_words.txt'
    with open(input_filename, 'r') as input_file:
        text = input_file.read()
    output_filename = 'output_files/count_words_output.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(str(count_words(text)))


if __name__ == '__main__':
    main()
