import numpy as np
import string
import argparse


def count_words(text):
    """Count words in a text.
    Return dictionary of the form {"word": count}
    """
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words, counts = np.unique(text.split(), return_counts=True)
    return dict(zip(words, counts))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', '-i', type=str,
                        default=None, help='Path to an input file.')
    parser.add_argument('--output-file', '-o', type=str,
                        default=None, help='Path to an output file.')
    args = parser.parse_args()
    input_filename = args.input_file
    if input_filename:
        with open(input_filename, 'r') as input_file:
            text = input_file.read()
    else:
        text = input()
    output_filename = args.output_file
    if output_filename:
        with open(output_filename, 'w') as output_file:
            output_file.write(str(count_words(text)))
    else:
        print(count_words(text))


if __name__ == '__main__':
    main()
