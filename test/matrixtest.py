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
        
    def testRotateRight(self):
        matrix1 = """
        12
        34
        56"""
        matrix2 = """
        531
        642
        """
        matrix1=Matrix(init_string=matrix1)
        matrix2=Matrix(init_string=matrix2)
        
        matrix1.rotate_right()
        self.assertEqual(str(matrix1),str(matrix2))

    def testRotateLeft(self):
        matrix1 = """
        12
        34
        56"""
        matrix2 = """
        246
        135
        """
        matrix1=Matrix(init_string=matrix1)
        matrix2=Matrix(init_string=matrix2)
        
        matrix1.rotate_left()
        self.assertEqual(str(matrix1),str(matrix2))
    
    def testRepr(self):
        matrix1 = """
        12
        34
        """
        matrix1=Matrix(init_string=matrix1)
        self.assertEqual(str(matrix1),"12\n34\n")

    def testSerialize(self):
        matrix1 = """
        12
        34
        """
        matrix1=Matrix(init_string=matrix1)
        
        self.assertEqual(matrix1.serialize(),[('1',0,0),('2',0,1),('3',1,0),('4',1,1)])

    def testSerializeWithFilter(self):
        matrix1 = """
        X2
        3X
        """
        matrix1=Matrix(init_string=matrix1)
        filter_fn=lambda value: True if value=='X' else False
        self.assertEqual(matrix1.serialize(filter_fn),[('X',0,0),('X',1,1)])
        
    def testInsert(self):
        matrix = """
        12
        34
        """
        matrix=Matrix(init_string=matrix)
        matrix.serial_set([('X',0,0),('Y',1,1)])
        self.assertEqual(str(matrix),"X2\n3Y\n")
    
    def testBeginRollback(self):
        matrix = Matrix(init_string="12\n34\n")
        matrix.begin()
        matrix.set('X', 0,0)
        self.assertEqual(str(matrix),"X2\n34\n")
        matrix.rollback()
        self.assertEqual(str(matrix),"12\n34\n")
        
    def testBeginCommit(self):
        matrix = Matrix(init_string="12\n34\n")
        matrix.begin()
        matrix.set('X', 0,0)
        self.assertEqual(str(matrix),"X2\n34\n")
        matrix.commit()
        self.assertEqual(str(matrix),"X2\n34\n")
        

    def testConditionalSet(self):
        matrix = Matrix(init_string=".X\n..\n")
        fn_validator =  lambda old_v, v: True if old_v=='.' else False
        matrix.serial_set([('*',0,0),['*',0,1]], fn_validator )
        self.assertEqual(str(matrix),".X\n..\n")
        matrix.serial_set([('*',0,0),['*',1,0]], fn_validator )
        self.assertEqual(str(matrix),"*X\n*.\n")

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMatrixConstructor']
    unittest.main()