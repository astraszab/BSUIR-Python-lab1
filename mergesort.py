import argparse


def merge(numbers, low, high, middle):
    """Merge two sorted arrays.
    """
    left_array = numbers[low:middle]
    right_array = numbers[middle:high]
    i = 0
    j = 0
    k = low
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            numbers[k] = left_array[i]
            i += 1
        else:
            numbers[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        numbers[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        numbers[k] = right_array[j]
        j += 1
        k += 1


def sort_in_bounds(numbers, low, high):
    """A recursive function for mergesort algorithm.
    """
    if low + 1 < high:
        middle = int((high + low) / 2)
        sort_in_bounds(numbers, low, middle)
        sort_in_bounds(numbers, middle, high)
        merge(numbers, low, high, middle)


def mergesort(numbers_string):
    """Sort values from a string in ascending order using mergesort.
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
    if input_filename:
        with open(input_filename, 'r') as input_file:
            numbers_string = input_file.read()
    else:
        numbers_string = input()
    output_filename = args.output_file
    if output_filename:
        with open(output_filename, 'w') as output_file:
            output_file.write(str(mergesort(numbers_string)))
    else:
        print(mergesort(numbers_string))


if __name__ == '__main__':
    main()
