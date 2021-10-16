from stringcolor import *
from sys import  getsizeof

class matrix:
    def __init__(self,demin,fill):
        self.rows=demin[0]
        self.col=demin[1]
        self.A=[
            [fill]*self.col
            for i in range(self.rows)
        ]
    def __str__(self):
        rows=len(self.A)
        ret=''
        for i in range(rows):
            cols=len(self.A[i])
            for j in range(cols):
                ret+=str(self.A[i][j])+"\t"
            ret+="\n"
        return ret
#%time tell how much time it will to execute the opertions
m=matrix((50,50),2)
#print(m)
print(getsizeof(cs(m,"red")))