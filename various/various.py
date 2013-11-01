'''
Created on 01/nov/2013

@author: minus
'''
import math
from sets import Set

def prime(x):
    if x<1:
        return False
    a = Set(range(2,x+1))
    num_limit = int(math.sqrt(x))
    for i in range(2,num_limit+1):
        if i in a :
            for n in range(x):
                y = i**2+n*i
                if y<=x:
                    if y in a:
                        a.remove(y)
                else:
                    break
    return x in a
    
def reverse(s):
    l=len(s)
    res = [' ' for _ in range(l)]
    for i,c in enumerate(s):
        res[l-i-1]=c
    return "".join(res)

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    result = reduce(lambda tot,c: tot+score[c],word,0)
    return result

def censor(phrase,block_word):
    words = phrase.split(' ')
    for i,word in enumerate(words):
        if word == block_word:
            words[i]='*'*len(word)
    return " ".join(words)

def remove_duplicates(a_list):
    result=[]
    for value in a_list:
        if value not in result:
            result.append(value)
    return result

def median(lst):
    lst=sorted(lst)
    mid = (len(lst)-1)/2
    mid_2 = (len(lst))/2
    return (lst[mid]+lst[mid_2])/2.0


if __name__ == '__main__':
    pass