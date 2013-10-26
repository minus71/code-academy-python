'''
Created on 24/ott/2013

@author: minus
'''

class Matrix():
    '''
    Simple 2d array class
    '''


    def __init__(self,rows,cols):
        '''
        Builds a new matrix
        '''
        self.rows=rows
        self.cols=cols
        self.__matrix = [[None]*cols for _ in range(rows)]
    
    def set(self,item,row,col):
        if col < self.cols and col>0:
            if row < self.rows and row >0:
                self.__matrix[row][col]=item

    def get(self,row,col):
        if col < self.cols and col>0:
            if row < self.rows and row >0:
                return self.__matrix[row][col]
        
    def array(self):
        return self.__matrix[:]