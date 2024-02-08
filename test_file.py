import unittest
from unittest.mock import patch
from exercise import generate_random_numbers, calculate_statistics, parse_command_line_arguments, get_slice_of_list

class TestRandomStats(unittest.TestCase):

    def test_generate_random_numbers(self):
        """Test if the random number generator produces a list of the correct size."""
        numbers = generate_random_numbers(100, 1, 1000)
        self.assertEqual(len(numbers), 100)
        for number in numbers:
            self.assertTrue(1 <= number <= 1000)

    def test_calculate_statistics(self):
        """Test the statistics calculation."""
        test_data = [1, 2, 3, 4, 5]
        mean, median = calculate_statistics(test_data)
        self.assertEqual(mean, 3)
        self.assertEqual(median, 3)

    def test_parse_command_line_arguments_valid(self):
        """Test the command line argument parsing with valid arguments."""
        test_args = ["random_stats.py", "10", "20"]
        with patch('sys.argv', test_args):
            start_index, end_index = parse_command_line_arguments()
            self.assertEqual(start_index, 10)
            self.assertEqual(end_index, 20)

    def test_parse_command_line_arguments_invalid(self):
        """Test the command line argument parsing with invalid arguments."""
        test_args = ["random_stats.py", "ten", "twenty"]
        with patch('sys.argv', test_args):
            with self.assertRaises(ValueError):
                parse_command_line_arguments()

    def test_get_slice_of_list(self):
        """Test the list slicing functionality."""
        test_list = list(range(100))
        start_index = 10
        end_index = 20
        sliced_list = get_slice_of_list(test_list, start_index, end_index)
        self.assertEqual(sliced_list, test_list[start_index:end_index])

    # You can add more tests to cover edge cases or possible errors.

if __name__ == '__main__':
    unittest.main()
