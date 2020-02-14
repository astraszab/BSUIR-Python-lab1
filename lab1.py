import argparse
from count_words import count_words
from most_frequent_words import most_frequent_words
from quicksort import quicksort
from mergesort import mergesort
from fibonacci import fibonacci_to_list


TASKS = {
'count-words': count_words,
'most-frequent-words': most_frequent_words,
'quicksort': quicksort,
'mergesort': mergesort,
'fibonacci': fibonacci_to_list,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', '-t', type=str,
                        required=True, help='Task to execute.',
                        choices=TASKS.keys())
    parser.add_argument('--input-file', '-i', type=str,
                        default=None, help='Path to an input file.')
    parser.add_argument('--output-file', '-o', type=str,
                        default=None, help='Path to an output file.')
    args = parser.parse_args()
    input_filename = args.input_file
    if input_filename is not None:
        with open(input_filename, 'r') as input_file:
            n = input_file.read()
    else:
        n = input()
    output_filename = args.output_file
    if output_filename is not None:
        with open(output_filename, 'w') as output_file:
            output_file.write(str(TASKS[args.task](n)))
    else:
        print(TASKS[args.task](n))


if __name__ == '__main__':
    main()
