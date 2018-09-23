import rn
import unittest

class TestRomanNumeral(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(rn.convert(1), 'I')
        self.assertEqual(rn.convert(2), 'II')
        self.assertEqual(rn.convert(5), 'V')
        self.assertEqual(rn.convert(9), 'IX')
        self.assertEqual(rn.convert(10), 'X')
        self.assertEqual(rn.convert(15), 'XV')
        self.assertEqual(rn.convert(30), 'XXX')
        self.assertEqual(rn.convert(40), 'XL')
        self.assertEqual(rn.convert(50), 'L')
        self.assertEqual(rn.convert(70), 'LXX')
        self.assertEqual(rn.convert(90), 'XC')
        self.assertEqual(rn.convert(93), 'XCIII')
        self.assertEqual(rn.convert(100), 'C')
        self.assertEqual(rn.convert(304), 'CCCIV')
        self.assertEqual(rn.convert(519), 'DXIX')
        self.assertEqual(rn.convert(699), 'DCXCIX')
        self.assertEqual(rn.convert(961), 'CMLXI')
        self.assertEqual(rn.convert(1000), 'M')
        self.assertEqual(rn.convert(2804), 'MMDCCCIV')
        self.assertEqual(rn.convert(3999), 'MMMCMXCIX')


if __name__ == '__main__':
    unittest.main()