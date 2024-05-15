import unittest
from calculator.add import add
from calculator.div import div
from calculator.mul import mul
from calculator.sub import sub

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(add(1,-7), -6)
        self.assertEqual(add(6,-6), 0)

    def test_sub(self):
        self.assertEqual(sub(6,3), 3)
        self.assertEqual(sub(1,-7), 8)
        self.assertEqual(sub(6,-6), 12)
    
    def test_mul(self):
        self.assertEqual(mul(6,3), 18)
        self.assertEqual(mul(1,-7), -7)
        self.assertEqual(mul(6,-6), -36)
    
    def test_div(self):
        self.assertEqual(div(6,3), 2)
        self.assertAlmostEqual(div(1,-7), -0.14285714285714285)
        self.assertEqual(div(12,3), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
