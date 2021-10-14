import math
import numpy as np
from stringcolor import *
from logging import raiseExceptions
import matplotlib.pyplot as plt
def make_img():
    i=np.array([[ [0.1,0.1,0.1],[0.2,0.1,0.3],[0.2,0.1,0.3] ],
                [ [0.1,0.1,0.1],[0.2,0.1,0.3],[0.2,0.1,0.3] ],
                [ [0.1,0.1,0.1],[0.2,0.1,0.3],[0.2,0.1,0.3]  ],
                [[0.1,0.1,0.1],[0.2,0.1,0.3],[0.2,0.1,0.3]]])
    _=plt.imshow(i)
    print(_)
    print(i.shape)
def sigmaoid(x):

    s=1./(1.+math.e**(-x))
    return s



y=np.random.seed(12)
zero=np.zeros((3,5))#intials 3,5 matrix with zeros
z=np.arange(1.0,20,1)
np.arange(0.5,15,1).reshape(5,3).shape
##################### BRODCASTING #################
brod=np.arange(4)
brodxx=brod.reshape(4,1)
xones=np.ones(6)
test=np.zeros(5)
zones=np.ones((3,4))
x=np.array(
    [
    [[1,2,3]
    ,[1,2,7],[1,2,2]
    ]
    ])
#print(cs(x.shape,"red"))
#print(cs(z[:10],"yellow"))
#print(z.shape)
#print(zero)
#sig=[1,2,3]
#sig=np.array(sig)
#print(sigmaoid(sig))
#print(brod.shape)
#print(brodxx.shape)
#print(xones.shape)
#print(test*brodxx+3)
def ar():
    x=np.zeros(4)
    x=x.reshape(4,1)

    z=np.array([1,23,2,3])
    print(x+z)
def normalizing():
    x=np.array([[1,2,3],[2,4,6]])
    y=np.amax(x,axis=1)
    y=y.reshape(2,1)
    print(y.shape)
    print(x.shape)
    try:
        z=x/y
    except:
        raiseExceptions
    finally:
        print(z)

#normalizing()
print(make_img())