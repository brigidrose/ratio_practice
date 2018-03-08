import unittest
from ratios import get_ratios

class RatioTest(unittest.TestCase):
    def test_ratios(self):
        self.assertEqual(get_ratios({}, 1), {})
        self.assertEqual(get_ratios({1: 1}, 2), {1: 2})
        self.assertEqual(get_ratios({1: 1}, 0), {1: 0})
        self.assertEqual(get_ratios({1: 1, 2: 1, 3: 1}, 11), {1: 4, 2: 4, 3: 3})
        self.assertEqual(get_ratios({1: 1, 2: 2, 3: 1}, 11), {1: 3, 2: 6, 3: 2})
        self.assertEqual(get_ratios({1: 0.5, 2: 1, 3: 0.5}, 11), {1: 3, 2: 6, 3: 2})


if __name__== '__main__':
    unittest.main()