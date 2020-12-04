import unittest
import code

class Test(unittest.TestCase):
    def test_part1(self):
        list = []
        with open("input.txt") as f:
            for line in f:
                list.append(line)
        self.assertEqual(code.main(list), 2)


unittest.main()
