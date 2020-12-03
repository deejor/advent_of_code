import unittest
import code


class Tests(unittest.TestCase):
    def test_part1(self):
        list = []
        with open("input.txt") as f:
            for line in f:
                list.append(int(line))
        self.assertEqual(code.part_1(list), 2020)

    def test_part2(self):
        list = []
        with open("input.txt") as f:
            for line in f:
                list.append(int(line))
        self.assertEqual(code.part_2(list), 2020)


unittest.main()
