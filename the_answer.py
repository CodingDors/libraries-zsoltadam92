




import sys
import random
import statistics

def generate_random_numbers(size, lower_bound, upper_bound):
    """Generate a list of random integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def calculate_statistics(numbers):
    """Calculate and return the mean and median of the numbers."""
    return statistics.mean(numbers), statistics.median(numbers)

def parse_command_line_arguments():
    """Parse command-line arguments and return as start and end indices for the slice."""
    if len(sys.argv) != 3:
        raise ValueError("Please provide two command-line arguments for slice start and end indices.")
    
    start_index = int(sys.argv[1])
    end_index = int(sys.argv[2])

    if start_index < 0 or end_index < 0:
        raise ValueError("Slice indices must be non-negative integers.")

    # Ensure this return statement is correctly indented to be part of the function
    return start_index, end_index

def get_slice_of_list(lst, start_index, end_index):
    """Return a slice of the list from start_index to end_index."""
    return lst[start_index:end_index]

def main():
    """Main function to generate numbers, calculate statistics, and print a slice based on command-line arguments."""
    random_numbers = generate_random_numbers(100, 1, 1000)
    mean, median = calculate_statistics(random_numbers)

    try:
        start_index, end_index = parse_command_line_arguments()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        numbers_slice = get_slice_of_list(random_numbers, start_index, end_index)
        print(f"Sliced list: {numbers_slice}")
    except IndexError as e:
        print(f"Error: {e}. Ensure that the provided slice indices are within the range of the list.")
        sys.exit(1)

    print(f"Mean: {mean:.2f}, Median: {median}")

if __name__ == "__main__":
    main()
