from stringcolor import *
import numpy as np
# what is difference between np.kron and np.outer product 
#Dot product of "matrix ,matrix multiplication" 
def kron_product1():
    return np.kron(np.ones((2,2)),np.identity(2))
def kron_product():
    """
    kron_product [difference between outer and kronecker product]

    [extended_summary]

    Returns:
        [matrix]: [kronecker product of two matrix]
    """
    a=np.arange(9).reshape(3,3)
    b=np.arange(16).reshape(4,4)
    print(cs(np.outer(a,b),"orange"))
    return np.kron(a,b)

def function1():                    
    """
    function1 [element vice multiplication]

    [extended_summary]
    """
    x=np.arange(9).reshape(3,3)
    y=np.arange(9).reshape(3,3)
    z=np.dot(x,y)
    print(z)
#A  = BAinv(B)
def inverse(A,B):
    """
    inverse [summary]

    [extended_summary]

    Args:
        A ([matrix 1]): [first matrix]
        B ([matrix 2]): [second matrix]
    """
    result=B*A*B.I
    return result
def inner_product(Martix_A,Martix_B):
    return np.inner(Martix_A,Martix_B)

if __name__=="__main__":

#print(kron_product())
    print(kron_product1())
# function1()
# print(inverse(np.matrix(np.random.rand(3,3))
#               ,np.matrix(np.random.rand(3,3))))
# print(inner_product(np.asmatrix(np.random.rand(4,4))
#               ,np.asmatrix(np.random.rand(4,4))))


