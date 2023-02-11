import unittest
import answer


class TestLast(unittest.TestCase):
    def test_gets_last(self):
        actual = answer.addNums(["2\n", "2\n", "3\n"])
        self.assertEqual(actual, 5)
    def more_nums(self):
        actual = answer.addNums(["5\n", "2\n", "3\n","2\n", "2\n", "3\n"])
        self.assertEqual(actual, 12)
    def test_handles_empty(self):
        actual = answer.addNums([])
        self.assertEqual(actual, "EMPTY")
    def Check_999(self):
        actual = answer.addNums([["5\n", "2\n", "-999\n","2\n", "2\n", "3\n"]])
        self.assertEqual(actual, 2)