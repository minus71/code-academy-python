'''
Created on 27/ott/2013

@author: minus
'''
import unittest
from navalbattle.board import Board, Ship
from UserString import MutableString
from sets import Set
from random import randrange



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
        for _ in range(10):
            expected.append(ocean*12)
            expected.append('\n')
        self.assertEqual(expected, str(board))
    
    def testShip(self):
        ship_txt = """
        ###*
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
     
    def testAddShip(self):
        ship_txt = """
        ##
        #
        """
        ship = Ship(ship_txt)
        self.assertEqual([(0,0),(0,1),(1,0)], ship.as_list())
        
    def testRandomize(self):
        board=Board()

        ship_txt = """
        ####
        ##
        """
        ship = Ship(ship_txt)
        board.add_ship(ship)

        ship_txt = """
        ###
        """
        ship = Ship(ship_txt)
        board.add_ship(ship)
        
        ship_txt = """
        ####
        """
        ship = Ship(ship_txt)

        board.add_ship(ship)
        ship_txt = """
        #
        """
        ship = Ship(ship_txt)
        board.add_ship(ship)
        board.randomize_map()
        
        board_string = str(board)
        
        num_ship_flag=0
        for c in board_string:
            if c == Board.SHIP:
                num_ship_flag+=1
        self.assertEqual(14, num_ship_flag, "This board has not the right number of ships:\n%s"%(str(board)));

    def testFire(self):
        board=Board()
        ship_txt = """
        ####
        """
        ship = Ship(ship_txt)

        board.add_ship(ship)
        ship_txt = """
        #
        """
        ship = Ship(ship_txt)
        board.add_ship(ship)
        board.randomize_map()
        
        ship_locations = Set(board.hidden_ships)
        r,c = ship_locations.pop()
        points,_ = board.fire(r,c)
        self.assertEqual(points, 1)
        
        points,message = board.fire(r,c)
        self.assertEqual(points, 0)
        self.assertEquals("Coordinates already hit.", message)
        print board.as_string(show_ship=False)
        
    def testRandomFire(self):
        board=Board()
        ship_txt = """
        ####
        """
        ship = Ship(ship_txt)

        board.add_ship(ship)
        ship_txt = """
        #
        """
        ship = Ship(ship_txt)
        board.add_ship(ship)
        board.randomize_map()
        
        ship_locations = Set(board.hidden_ships)

        for _ in range(20):
            r=randrange(board.rows)
            c=randrange(board.cols)
            points,_ = board.fire(r,c)
            if (r,c) in ship_locations:
                self.assertEqual(points, 1)
                ship_locations.remove((r,c))
            else:
                self.assertEqual(points, 0)
        
        print board.as_string()
        
    
#     @patch('sys.stdout', new_callable=StringIO)
#     def testPrint(self):
#         board = Board()
#         board.randomize_map()
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()