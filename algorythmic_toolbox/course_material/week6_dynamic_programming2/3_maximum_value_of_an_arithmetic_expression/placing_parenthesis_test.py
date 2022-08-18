
import unittest
from placing_parentheses import get_maximum_value

class TestParenthesis(unittest.TestCase):
    
    def test_01(self):
        self.assertEqual(6, get_maximum_value('1+5'))
    
    def test_02(self):
        self.assertEqual(0, get_maximum_value('1+2-3'))
    
    def test_03(self):
        self.assertEqual(9, get_maximum_value('1+2*3'))
    
    def test_04(self):
        self.assertEqual(0, get_maximum_value('1+2-3*4'))
    
    def test_05(self):
        self.assertEqual(200, get_maximum_value('5-8+7*4-8+9'))
    
    def test_06(self):
        self.assertEqual(6, get_maximum_value('1+2-3*4-5'))


if __name__ == '__main__':
    unittest.main()