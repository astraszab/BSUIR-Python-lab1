import argparse


def generate_fibonacci(n):
    """Generate first n Fibonacci numbers
    """
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_to_list(n):
    """Return a list of first n Fibonacci numbers.
    """
    n = int(n)
    return list(generate_fibonacci(n))


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
            n = input_file.read()
    else:
        n = input()
    output_filename = args.output_file
    if output_filename:
        with open(output_filename, 'w') as output_file:
            output_file.write(str(fibonacci_to_list(n)))
    else:
        print(fibonacci_to_list(n))


if __name__ == '__main__':
    main()
