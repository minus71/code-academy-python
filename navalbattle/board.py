'''
Created on 27/ott/2013

@author: minus
'''
from UserString import MutableString
from random import randrange
from sets import Set
from logging import warn

class Board():
    '''
    A naval battle game board
    '''
    OCEAN='~'
    SHIP='#'    
    HIT='*'    
    MISS='X'
    OUT_OF_BOARD='0'    
    def __init__(self,rows=10,cols=10):
        '''
        Builds a new boad
        '''
        rows = min(64,rows)
        rows = max(10,rows)
        cols = min(64,cols)
        cols = max(10,cols)
        self.rows=rows
        self.cols=cols
        self.ships=[]
        self.hidden_ships=Set()
        self.hit=Set()
        self.miss=Set()
        
    def dim(self):
        return self.rows,self.cols
    
    def print_board(self):
        print self.as_string(show_ship=False)


    def fire_result(self, r, c):
        if r not in range(self.cols) or r not in range(self.rows):
            return Board.OUT_OF_BOARD 
        coord = r, c
        if coord in self.hit:
            result = Board.HIT
        elif coord in self.hidden_ships:
            result = Board.SHIP
        elif coord in self.miss:
            result = Board.MISS
        else:
            result = Board.OCEAN
        return result

    def as_string(self,show_hit=True,show_ship=True,show_miss=True):
        out_buffer = MutableString()
        for r in range(self.rows):
            for c in range(self.cols):
                coord = r, c
                if coord in self.hit and show_hit:
                    result = Board.HIT
                elif coord in self.hidden_ships and show_ship:
                    result = Board.SHIP
                elif coord in self.miss and show_miss:
                    result = Board.MISS
                else:
                    result = Board.OCEAN
                
                out_buffer.append(result)
            out_buffer.append('\n')
        
        return out_buffer

    def __repr__(self):
        out_buffer = self.as_string()
        return str(out_buffer)

    def add_ship(self, *ships):
        for ship in ships:
            self.ships.append(ship)
    
    def randomize_map(self):
        for ship in self.ships:
            unplaced = True
            i = 0
            while unplaced:
                i+=1
                if i>1000:
                    # To prevent loops on unplaceble ships
                    warn('Could not set ship on board')
                delta_col=ship.cols-1
                delta_row=ship.rows-1
                off_row = randrange(self.rows-delta_row)
                off_col = randrange(self.cols-delta_col)
                coords = ship.as_list()
                unplaced=False
                new_set=Set()
                for coord in coords:
                    r,c = coord[0]+off_row,coord[1]+off_col
                    if c >= self.cols or r>=self.rows:
                        unplaced=True
                        break
                    else:
                        new_set.add((r,c))
                        
                if not unplaced:
                    extended_set = Set(new_set)
                    for coord in new_set:
                        r,c = coord
                        extended_set.add((r,c+1))
                        extended_set.add((r,c-1))
                        extended_set.add((r+1,c))
                        extended_set.add((r-1,c))
                    if len(self.hidden_ships.intersection(extended_set))>0:
                        unplaced=True
                    
                if not unplaced:
                    self.hidden_ships=self.hidden_ships.union(new_set)

    def fire(self,row,col):
        result = self.fire_result(row, col)
        if result in (Board.HIT,Board.MISS):
            return 0,"Coordinates already hit."
        elif result == Board.OUT_OF_BOARD:
            return 0,"Try to hit the board!"
        else:
            coord = (row,col)
            if coord in self.hidden_ships:
                self.hit.add(coord)
                return 1, "Hit!!!"
            else:
                self.miss.add(coord)
                return 0, "Miss."

        
    def avialable_targets(self):
        return len(self.hidden_ships) - len(self.hit)
        


class Ship():
    
    def __init__(self,as_string):
        lines = as_string.splitlines()
        self.__matrix=[]
        min_col = 9999
        max_col = 0

        for row in lines:
            if not row.isspace() and not len(row)==0:
                self.__matrix.append(row)
                for i in range(len(row)):                    
                    c=row[i]
                    if not c.isspace():
                        min_col=min(min_col,i)
                        max_col=max(max_col,i)
        self.rows = len(self.__matrix)
        self.cols = max_col+1 - min_col
        for i in range(len(self.__matrix)):
            str_row=self.__matrix[i]
            char_array = []
            for j in range(min_col,max_col+1):
                if len(str_row)>j:
                    chr_val = str_row[j]
                    if chr_val.isspace():   
                        char_array.append(' ')
                    else:
                        char_array.append('#')
                else:
                    char_array.append(' ')
            self.__matrix[i]=char_array
    
    def __repr__(self):
        out_buffer=MutableString()
        for r in range(self.rows):
            for c in range(self.cols):
                out_buffer.append(self.__matrix[r][c])
            out_buffer.append('\n')
        return str(out_buffer)

    def rotate(self,ticks=1):
        ticks=ticks%4
        for _ in range(ticks):
            matrix = [[' ']*self.rows for _ in range(self.cols)]
            for r in range(self.rows):
                for c in range(self.cols):
                    matrix[c][self.rows-r-1]=self.__matrix[r][c]
            self.__matrix=matrix
            self.cols,self.rows=self.rows,self.cols
    
    def as_list(self):
        rows,cols,matrix = self.rows,self.cols,self.__matrix
        _list = []
        for r in range(rows):
            for c in range(cols):
                value = matrix[r][c]
                if value!=' ':
                    _list.append((r,c))
        return _list
                

class Game():
    
    CARRIER=Ship("####\n##")
    CRUISER=Ship("###")
    DESTROYER=Ship("##")
    SUBMARINE=Ship("#")
    
    def __init__(self,players=2,turns=5,carriers=1,cruisers=3,destroyer=5,submarines=4,board_dimensions=(10,15)):
        rows,cols=board_dimensions
        self.board=Board(rows,cols)            
        for _ in range(carriers):
            self.board.add_ship(Game.CARRIER)
        for _ in range(cruisers):
            self.board.add_ship(Game.CRUISER)
        for _ in range(destroyer):
            self.board.add_ship(Game.DESTROYER)
        for _ in range(submarines):
            self.board.add_ship(Game.SUBMARINE)
        self.scores={}
        for n in range(players):
            self.scores[n]=0
        self.turns=turns
        self.current_turn=0
    
    def play(self):
        self.board.randomize_map()
        for turn in range(self.turns):  
            self.turn(turn)
            if self.board.avialable_targets()==0:
                break
        print "Game Over"
        max_score = 0
        top_players=[] 
        for p in self.scores:
            score = self.scores[p]
            if score>max_score:
                top_players=[p]
                max_score=score
            if score == max_score:
                top_players.append(p)
        
        if len(top_players)==1:
            print "Player %d wins!" % (top_players[0])
        else:
            print "Game is a draw for the following players:"
            for p in top_players:
                print "Player %d" %(p)
        
        print self.board.as_string()
        

    def turn(self,turn):
        for player in self.scores:
            self.player_turn(player,turn)
    
    def player_turn(self,player,turn):
        print "Turn %d for player %d" % (turn,player)
        print "  current score: %d" %(self.scores[player])
        self.board.print_board()
        row = raw_input("Insert row coord:  ")
        col= raw_input( "Insert colum coord:")
        score,msg = self.board.fire(int(row), int(col))
        self.scores[player]+=score
        print msg
        print "  current score: %d" %(self.scores[player])
        self.board.print_board()
        
        