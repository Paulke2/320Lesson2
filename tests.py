import unittest
import answer


class TestLast(unittest.TestCase):
    def test_addNums(self):
        actual = answer.addNums(["2\n", "2\n", "3\n"])
        self.assertEqual(actual,"5")
    def test_more_nums(self):
        actual = answer.addNums(["5\n", "2\n", "3\n","2\n", "2\n", "3\n"])
        self.assertEqual(actual, "12")
    def test_handles_empty(self):
        actual = answer.addNums([])
        self.assertEqual(actual, "EMPTY")
    def test_Check_999(self):
        actual = answer.addNums(["4\n", "2\n", "-999\n","2\n", "2\n", "3\n"])
        self.assertEqual(actual, "2")

    def test_negatives(self):
        actual = answer.addNums(["5\n", "2\n", "20\n", "-2\n", "-2\n", "3\n","-999\n"])

        self.assertEqual(actual,"25")

    def test_zero(self):
        actual = answer.addNums(["5\n", "-999\n", "20\n", "-2\n", "-2\n", "3\n", "-4\n"])

        self.assertEqual(actual, "0")

    def test_all_negatives(self):
        actual = answer.addNums(["5\n", "-2\n", "-20\n", "-2\n", "-2\n", "-3\n", "-999\n"])

        self.assertEqual(actual, "0")

    #testing sumNums
    def test_sumNums(self):
        actual =answer.sumNums(["4\n", "2\n","2\n", "2\n", "3\n"])
        self.assertEqual(actual, 13)
    def test_sumNums_with_999(self):
        actual = answer.sumNums(["4\n", "2\n", "-999\n", "2\n", "2\n", "3\n"])
        self.assertEqual(actual, 6)

    def test_sumNums_999_first(self):
        actual = answer.sumNums(["-999\n", "-999\n","2\n", "2\n", "2\n", "3\n"])
        self.assertEqual(actual, 0)
    def test_sumNums_999_last(self):
        actual = answer.sumNums(["4\n", "2\n", "4\n", "2\n", "2\n","-999\n"])
        self.assertEqual(actual, 14)