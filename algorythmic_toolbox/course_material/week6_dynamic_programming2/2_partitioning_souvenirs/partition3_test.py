import unittest
import numpy as np

from partition3 import partition3# construct_divisible_souvenirs3

class TestPartition3(unittest.TestCase):
    
    def test_01(self):
        A = [3, 3, 3, 3]
        self.assertFalse(bool(partition3(A)))
        
    def test_02(self):
        A = [40]
        self.assertFalse(bool(partition3(A)))
    
    def test_03(self):
        A = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
        self.assertTrue(bool(partition3(A)))
        
    def test_04(self):
        A = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
        self.assertTrue(bool(partition3(A)))
        
    def test_05(self):
        A = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 2, 2]
        self.assertTrue(bool(partition3(A)))
        
    def test_06(self):
        A = [0, 0, 1, 1, 1]
        self.assertRaises(ValueError, partition3, A)
        
    def test_07(self):
        A = [3, 1, 1, 1, 1, 1, 1]
        self.assertTrue(bool(partition3(A)))
        
    def test_08(self):
        A = [13, 31, 9, 35, 10, 12, 6, 16]
        self.assertTrue(bool(partition3(A)))
        
    def test_09(self):
        A = [1, 2]
        self.assertFalse(bool(partition3(A)))
        
    def test_10(self):
        A = [1, 1, 1]
        self.assertTrue(bool(partition3(A)))
        
    def test_11(self):
        
        for kk in range(0, 10000):
            np.random.seed(kk)
            
            n = np.random.randint(3,20)
            A = [0] * n
            S = np.random.randint(1, 30*(n // 3))
            for s in ((0, n // 3),
                      (n // 3, (n // 3) *2),
                      ((n // 3)*2, n)):
                for ii in range(s[0], s[1]):
                    if ii < s[1]-1:
                        A[ii] = np.random.randint(1, 30)
                    else:
                        A[ii] = S - sum(A[s[0]:ii])
            if min(A) <= 0:
                continue
            will_fail = np.random.randint(0,2)
            A[-1] = A[-1] + will_fail
            
            if bool(will_fail):
                self.assertFalse(bool(partition3(A)))
            else:
                self.assertTrue(bool(partition3(A)))

#   def test_12(self):
#       A = [13, 31, 9, 35, 10, 12, 6, 16]
#       construct_divisible_souvenirs3(A)
        
if __name__ == '__main__':
    unittest.main()
#    TestPartition3().test_12()