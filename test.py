import rn
import unittest

class TestRomanNumeral(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(rn.convert(1), 'I')
        self.assertEqual(rn.convert(2), 'II')


if __name__ == '__main__':
    unittest.main()