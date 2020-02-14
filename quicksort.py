import argparse


def make_partition(numbers, low, high):
    """Make the partition of an array for quicksort.
    """
    partition_index = high - 1             # Where partition should be
    current_partition_position = high - 1  # Where partition currently is
    partition = numbers[current_partition_position]
    i = 0
    while i <= partition_index:
        if numbers[i] <= partition:
            i += 1
        else:
            numbers[i], numbers[partition_index] = \
                numbers[partition_index], numbers[i]
            partition_index -= 1
            if numbers[i] == partition:
                current_partition_position = i
    numbers[partition_index], numbers[current_partition_position] = \
        numbers[current_partition_position], numbers[partition_index]
    return partition_index


def sort_in_bounds(numbers, low, high):
    """A recursive function for quicksort algorithm.
    """
    if low < high:
        partition_index = make_partition(numbers, low, high)
        sort_in_bounds(numbers, low, partition_index)
        sort_in_bounds(numbers, partition_index + 1, high)


def quicksort(numbers_string):
    """Sort values from a string in ascending order using quicksort.
    """
    numbers = [int(number) for number in numbers_string.split()]
    sort_in_bounds(numbers, 0, len(numbers))
    return numbers


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
            numbers_string = input_file.read()
    else:
        numbers_string = input()
    output_filename = args.output_file
    if output_filename is not None:
        with open(output_filename, 'w') as output_file:
            output_file.write(str(quicksort(numbers_string)))
    else:
        print(quicksort(numbers_string))


if __name__ == '__main__':
    main()
