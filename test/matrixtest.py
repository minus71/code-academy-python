'''
Created on 24/ott/2013

@author: minus
'''
import unittest
from navalbattle.matrix import Matrix


class Test(unittest.TestCase):


    def testMatrixConstructor(self):
        matrix = Matrix(3,2)
        self.assertIsNotNone(matrix)
    
    def testGetRows(self):
        matrix = Matrix(3,2)
        self.assertEqual(matrix.rows, 3)

    def testGetCols(self):
        matrix = Matrix(3,2)
        self.assertEqual(matrix.cols, 2)
    

    def testGetItem(self):
        matrix = Matrix(3,2)
        matrix.set("X",1,1)
        item = matrix.get(1,1)
        self.assertEqual("X", item)

    def testGetItemNone(self):
        matrix = Matrix(3,2)
        matrix.set("X",5,5)
        item = matrix.get(5,5)
        self.assertIsNone(item)

    def testGetArray(self):
        matrix = Matrix(3,2)
        my_array = matrix.array()
        self.assertIsNotNone(my_array)

    def testInitWithString(self):
        astr = """
        12
        34
        56
        """
        matrix = Matrix(init_string=astr)
        self.assertEqual(['1','2'], matrix.array()[0])
        self.assertEqual(['3','4'], matrix.array()[1])
        self.assertEqual(['5','6'], matrix.array()[2])
        
    def testInitWithString2(self):
        astr = """
         2
        3
        56
        """
        matrix = Matrix(init_string=astr)
        self.assertEqual([' ','2'], matrix.array()[0])
        self.assertEqual(['3',' '], matrix.array()[1])
        self.assertEqual(['5','6'], matrix.array()[2])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMatrixConstructor']
    unittest.main()