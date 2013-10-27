'''
Created on 27/ott/2013

@author: minus
'''
from UserString import MutableString

class Board():
    '''
    A naval battle game board
    '''
    OCEAN='~'
    
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

    def dim(self):
        return self.rows,self.cols
    
    def __repr__(self):
        out_buffer=MutableString()
        for r in range(self.rows):
            for c in range(self.cols):
                out_buffer.append(Board.OCEAN)
            out_buffer.append('\n')
        return str(out_buffer)

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
                    char_array.append(str_row[j])
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
        

