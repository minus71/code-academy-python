'''
Created on 24/ott/2013

@author: minus
'''
from UserString import MutableString

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
    
    def rotate_right(self):
        def clockwise (value,ir,ic,context):
            matrix = context['matrix']
            rows = matrix.rows
            cols = matrix.cols
            return value, ic,(rows-1)-ir
        
        self.transform(clockwise)

    def rotate_left(self):
        def clockwise (value,ir,ic,context):
            matrix = context['matrix']
            rows = matrix.rows
            cols = matrix.cols
            return value, (cols-1)-ic,ir
        self.transform(clockwise)
        
    
    
    def traverse(self,handler_function):
        for ir in range(self.rows):
            for ic in range(self.cols):
                value = self.__matrix[ir][ic]
                result = handler_function(value,ir,ic)
                if result:
                    self.__matrix[ir,ic]
    
    def transform(self,handler_function):
        out_matrix = {}
        context = {'matrix':self}
        max_row=-1
        max_col=-10
        for ir in range(self.rows):
            for ic in range(self.cols):
                value = self.__matrix[ir][ic]
                value_2,ir2,ic2 = handler_function(value,ir,ic,context)
                out_matrix[(ir2,ic2)]=value_2
                max_row=max(max_row,ir2)
                max_col=max(max_col,ic2)
        new_matrix = [[None]*(max_col+1) for _ in range(max_row+1)]
        for key in out_matrix:
            value = out_matrix[key]
            r,c = key
            new_matrix[r][c]=value
        self.__matrix=new_matrix
        self.cols=max_col+1
        self.rows=max_row+1
        
    def __repr__(self):
        outstr = MutableString("")
        for r in self.__matrix:
            outstr.append("".join(r)+"\n")
        return str(outstr)
                    
    def serialize(self):
        serial_matrix = []
        def serialize_function(value,ir,ic):
            serial_matrix.append((value,ir,ic))
        self.traverse(serialize_function)                     
        return serial_matrix
        
    def serial_set(self,serial_data):
        for val,row,col in serial_data:
            self.__matrix[row][col]=val
    
    