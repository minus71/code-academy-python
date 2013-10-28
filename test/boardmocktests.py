'''
Created on 28/ott/2013

@author: minus
'''
import unittest
from navalbattle.board import Game
from mock import patch
from StringIO import StringIO


class Test(unittest.TestCase):

    @patch('sys.stdout',new_callable=StringIO)
    def testBoardPrint(self,mock_stdout):
        game = Game()
        board = game.board
        board.randomize_map()
        expect= \
"""             1    
   012345678901234
 0 ~~~~~~~~~~~~~~~
 1 ~~~~~~~~~~~~~~~
 2 ~~~~~~~~~~~~~~~
 3 ~~~~~~~~~~~~~~~
 4 ~~~~~~~~~~~~~~~
 5 ~~~~~~~~~~~~~~~
 6 ~~~~~~~~~~~~~~~
 7 ~~~~~~~~~~~~~~~
 8 ~~~~~~~~~~~~~~~
 9 ~~~~~~~~~~~~~~~
"""
        board.print_board()
        actual=mock_stdout.getvalue()
        self.assertEqual(expect, actual,"Expect:\n%s \nis different from:\n%s"%(expect,actual))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBoardPrint']
    unittest.main()