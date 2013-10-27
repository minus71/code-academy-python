'''
Created on 27/ott/2013

@author: minus
'''
import unittest
from navalbattle.board import Board, Ship
from UserString import MutableString


class Test(unittest.TestCase):


    def testName(self):
        board = Board()
        self.assertIsNotNone(board)

    def testGetDimensions(self):
        board = Board()
        rows,cols=board.dim()
        self.assertEqual(10, rows)
        self.assertEqual(10, cols)

    def testGetDimensionsSet(self):
        board = Board(16,12)
        rows,cols=board.dim()
        self.assertEqual(16, rows)
        self.assertEqual(12, cols)

    def testGetDimensionsSetWithLimit(self):
        board = Board(500,12)
        rows,cols=board.dim()
        self.assertEqual(64, rows)
        self.assertEqual(12, cols)

        board = Board(2,120)
        rows,cols=board.dim()
        self.assertEqual(10, rows)
        self.assertEqual(64, cols)
        
    def testRepr(self):
        board=Board(10,12)
        ocean = '~'
        expected = MutableString()
        for i in range(10):
            expected.append(ocean*12)
            expected.append('\n')
        self.assertEqual(expected, str(board))
    
    def testShip(self):
        ship_txt = """
        ####
        ##
        """
        ship = Ship(ship_txt)
        self.assertEqual("####\n##  \n", str(ship))
        
    def testShipRotate(self):
        ship_txt = """
        ####
        ##
        """
        ship_rotated_txt = """
        ##
        ##
         #
         #        
        """
        ship = Ship(ship_txt)
        ship.rotate()
        ship_rotated = Ship(ship_rotated_txt)
        self.assertEqual(str(ship_rotated), str(ship))

    def testShipRotate2(self):
        ship_txt = """
        ####
        ##
        """
        ship_rotated_txt = """
          ##
        ####
        """
        ship = Ship(ship_txt)
        ship.rotate(2)
        ship_rotated = Ship(ship_rotated_txt)
        self.assertEqual(str(ship_rotated), str(ship),"Expected: \n%s\nActual:\n%s"%(ship_rotated,ship))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()