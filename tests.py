import unittest
import answer


class TestLast(unittest.TestCase):
    def test_gets_last(self):
        actual = answer.addNums(["2\n", "2\n", "3\n"])
        self.assertEqual(actual, 5)

    def test_handles_empty(self):
        actual = answer.print_all_lines([])
        self.assertEqual(actual, None)