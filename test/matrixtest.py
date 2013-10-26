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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMatrixConstructor']
    unittest.main()