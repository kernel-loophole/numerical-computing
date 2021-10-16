import numpy as np
from stringcolor import *
def simple_numpy_array():
    """[simple numpy array]


    """
    create=np.array([[1,2],[3,4]])
    print(cs("Shape of array","red"))
    print(cs(create.shape,"green"))
    print("Size of array")
    print(cs(create.size,"green"))
    print("Dimensions of array")
    print(cs(create.ndim,"green"))
def numpy_Data_type():
    data1=np.array([[1,2,3],[3,4,3],[5,6,3],[4,5,3]],dtype=np.int64)
    data2=np.array([[1,2],[3,4],[5,6]],dtype=np.complex128)
    data3=np.array([[1,2],[3,4],[5,6]],dtype=np.float128)
    print(cs(data1.shape,"green"))
   
    print(data2.real,data2.imag)
def fill_with():
    fill=np.zeros(10)
    fill_1=np.ones(10)#fill 10 value with 0
    fill_3=np.arange(1,10,2)#start,end,step
    fill_4=np.linspace(1,10,20)#start,end value,total value filled
    fill_5=np.logspace(1,3,5)# create five data sets start form 10*1  to 10*3
    print(fill,fill_1,fill_3)
def create_matrix():
    two_dim=np.identity(4)#make an identiy matrix of 4*4 with one's at diagonal
    dia_dim=np.diag(np.arange(0,20,5))
    print(cs(dia_dim,"green")) 
    print(two_dim)

    ##########spacial index case##########
    print(dia_dim[0:20:5])#start,end,step
def multi_dim():
    fun=lambda m,n:n*10+m+2
    make_array=np.fromfunction(fun,(5,5))
    return make_array

simple_numpy_array()
numpy_Data_type()
print(fill_with())
create_matrix()
print(multi_dim())