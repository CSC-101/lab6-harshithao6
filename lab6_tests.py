import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        books = [data.Book("Tolkien","The Hobbit"), data.Book("Jane Austen","Pride and Prejudice"), data.Book("Harper Lee","To Kill a Mockingbird")]
        expected = [data.Book("Jane Austen","Pride and Prejudice"),data.Book("Tolkien","The Hobbit"), data.Book("Harper Lee","To Kill a Mockingbird")]
        test = lab6.selection_sort_books(books)
        self.assertEqual(expected,test)

    def test_selection_sort_books2(self):
        books = [data.Book("J.K rowling","Harry Potter"), data.Book("Tolkien","Lord of rings"), data.Book("Paulo Coelho","The Alchemist")]
        expected = [data.Book("J.K rowling","Harry Potter"),data.Book("Tolkien","Lord of rings"),data.Book("Paulo Coelho","The Alchemist")]
        test = lab6.selection_sort_books(books)
        self.assertEqual(expected,test)

    # Part 2

    def test_swap_case_1(self):
        input =  "Hello, World"
        expected = "hELLO, wORLD"
        test = lab6.swap_case(input)
        self.assertEqual(test,expected)

    def test_swap_case_2(self):
        input =  "PyThOn"
        expected = "pYtHoN"
        test = lab6.swap_case(input)
        self.assertEqual(test,expected)

    # Part 3
    def test_str_translate_1(self):
        expected = "xbcdcbx"
        test = lab6.str_translate("abcdcba","a","x")
        self.assertEqual(test,expected)

    def test_str_translate_2(self):
        expected = "heppo"
        test = lab6.str_translate("hello", "l", "p")
        self.assertEqual(test, expected)

    # Part 4
    def test_histogram_1(self):
        input_str = "apple banana apple orange banana apple"
        test = lab6.histogram(input_str)
        expected_output = {
            'apple': 3,
            'banana': 2,
            'orange': 1
        }
        self.assertEqual(test,expected_output)

    def test_histogram_2(self):
        input_str = "one two two three three three"
        test = lab6.histogram(input_str)
        expected_output = {
            'one': 1,
            'two': 2,
            'three': 3
        }
        self.assertEqual(test,expected_output)


if __name__ == '__main__':
    unittest.main()
