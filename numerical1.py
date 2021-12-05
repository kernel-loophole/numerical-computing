import numpy as np
from stringcolor import *
def index():
    fn=lambda m,n:n*10+m
    x=np.fromfunction(fn,(5,5))
    print(cs(x.flatten(),"red"))
    print(x)
    print(x[1::5,0:3])
def merage():
    arr1=np.arange(1,10)
    arr1=arr1[np.newaxis,np.newaxis]# same as   np.expand_dims(data, axis=1)
    print(np.vstack((arr1,arr1)))#verticla stack ----------->np.concatenate
    print(np.hstack((arr1,arr1))) #horizontal stack
def borad():
    arr1=np.array([[1,2],[3,4]])
    arr2=np.array([[1,2]])
    print(arr1.shape,arr2.shape)
    print(arr1+arr2)

                                                  

index()
merage()
borad()