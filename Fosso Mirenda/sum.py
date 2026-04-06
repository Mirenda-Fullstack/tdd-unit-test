import unittest

def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):
    
    def test_sumfunc_1(self):
        a = 10
        b = 2
        result = sum(a, b)
        self.assertEqual(result, a + b)

    def test_sumfunct_2(self):
        a = 5
        b = 7
        result = sum(a, b)
        self.assertEqual(result, b + a)


if __name__ == "__main__":
    unittest.main()