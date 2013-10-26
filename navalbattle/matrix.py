'''
Created on 24/ott/2013

@author: minus
'''

class Matrix():
    '''
    Simple 2d array class
    '''


    def __init__(self,rows=None,cols=None,init_string=None):
        '''
        Builds a new matrix
        '''
        if rows :
            self.rows=rows
            self.cols=cols
            self.__matrix = [[None]*cols for _ in range(rows)]
        else:
            lines = init_string.splitlines()
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
            for i in range(len(self.__matrix)):
                str_row=self.__matrix[i]
                char_array = []
                for j in range(min_col,max_col+1):
                    if len(str_row)>j:
                        char_array.append(str_row[j])
                    else:
                        char_array.append(' ')
                self.__matrix[i]=char_array
            
        
    
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