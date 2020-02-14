import numpy as np
import string
import argparse


def most_frequent_words(text):
    """Return a string of 10 most frequent words in a text."""
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words, counts = np.unique(text.split(), return_counts=True)
    if len(words) == 0:
        return ''
    _, frequent_words = zip(*sorted(zip(counts, words), reverse=True))
    if len(frequent_words) > 10:
        frequent_words = frequent_words[:10]
    return ' '.join(frequent_words)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', '-i', type=str,
                        default=None, help='Path to an input file.')
    parser.add_argument('--output-file', '-o', type=str,
                        default=None, help='Path to an output file.')
    args = parser.parse_args()
    input_filename = args.input_file
    if input_filename is not None:
        with open(input_filename, 'r') as input_file:
            text = input_file.read()
    else:
        text = input()
    output_filename = args.output_file
    if output_filename:
        with open(output_filename, 'w') as output_file:
            output_file.write(most_frequent_words(text))
    else:
        print(most_frequent_words(text))


if __name__ == '__main__':
    main()
