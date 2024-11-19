import sys


def read_and_sum_file(filename: str):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    # Split the line and attempt to convert to floats
                    values = line.split()
                    if len(values) != 2:
                        raise ValueError(f"Line {line_num}: Missing or extra value")
                    num1, num2 = float(values[0]), float(values[1])
                    print(f"Line {line_num} sum: {num1 + num2}")
                except ValueError as e:
                    print(f"Error processing line {line_num}: {e}")
    except FileNotFoundError:
        print("Error: File not found or could not be opened.")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python file.py <filename>")
        sys.exit(1)

    read_and_sum_file(sys.argv[1])
