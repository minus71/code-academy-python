'''
Created on 01/nov/2013

@author: minus
'''
import unittest
from various.various import *


class Test(unittest.TestCase):


    def testPrime(self):
        self.assertFalse(prime(49))
        self.assertTrue(prime(53))
        self.assertFalse(prime(-53))
        self.assertFalse(prime(-49))
        self.assertFalse(prime(-2))

    def testReverse(self):
        self.assertEqual(reverse("ABCDE"),"EDCBA")

    def testScarbbleScore(self):
        some_score = scrabble_score("fungus")
        self.assertEqual(some_score,10)
        
        
    def testCensor(self):
        result = censor("some word are better not spoken","word")
        self.assertEqual(result, "some **** are better not spoken")
        
    def testDuplicates(self):
        result = remove_duplicates([1,2,3,3,4,5,1,6,7,7])
        self.assertEqual(result, [1,2,3,4,5,6,7])
        
    def testMedian(self):
        self.assertEqual(median([5,4,4,5]),4.5)
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrime']
    unittest.main()