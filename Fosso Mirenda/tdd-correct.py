import unittest

def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):
    def test_sum_func_1(self):
      a = 2
      b = 3
      result = sum(a, b)
      self.assertEqual(result, a + b)

if __name__ == "__main__":
    unittest.main()