'''
Created on 27/ott/2013

@author: minus
'''
from UserString import MutableString
from random import randint, randrange
from sets import Set
from logging import log, warn

class Board():
    '''
    A naval battle game board
    '''
    OCEAN='~'
    SHIP='#'    
    SHIP='*'    
    MISS='X'    
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

    def as_string(self,show_hit=True,show_ship=True,show_miss=True):
        out_buffer = MutableString()
        for r in range(self.rows):
            for c in range(self.cols):
                coord = r, c
                if coord in self.hit:
                    out_buffer.append(Board.HIT)
                elif coord in self.hidden_ships:
                    out_buffer.append(Board.SHIP)
                elif coord in self.miss:
                    out_buffer.append(Board.MISS)
                else:
                    out_buffer.append(Board.OCEAN)
            
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
                    break
                if i>10:
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
                

