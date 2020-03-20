import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

class EmtFunctions(object):

    def __init__(self, n):
        super().__init__()
        self.n=n
        self.nn=pow(2,n)

    # EMT instance: EMT_xorb
    def xorb(self,x,y,b):
        z=x^y^b
        return z

    # EMT instance: EMT_addb
    def addb(self,x,y,b):
        z= (x+y+b) % self.nn
        return z

    # EMT instance: EMT_xoraddb
    def xoraddb(self,x,y,b):
        z= (x^y+b) % self.nn
        return z
    
    # EMT instance: EMT_addxorb
    def addxorb(self,x,y,b):
        z= ((x+y) % self.nn)^b
        return z

# Demonstration 1 of four typical EMT instances for 8-bit keys
def test1():
    ef=EmtFunctions(8)
    n=8
    nn=pow(2,n)
    x=28892% nn
    b=21% nn

    ef1=[]
    ef2=[]
    ef3=[]
    ef4=[]
    for i in range(nn):
        y=i
        ef1.append(ef.xorb(x,y,b))
        ef2.append(ef.addb(x,y,b))
        ef3.append(ef.xoraddb(x,y,b))
        ef4.append(ef.addxorb(x,y,b))

        #print(i,ef.xorb(x,y,b),ef.addb(x,y,b),ef.xoraddb(x,y,b),ef.addxorb(x,y,b))
    print('n:{},x:{},b:{}'.format(8,x,b))
    plt.figure()
    t=range(nn)

    p21=plt.plot(t,ef1,color='b',  marker='*')
    p22=plt.plot(t,ef2,color='y',  marker='v')
    p23=plt.plot(t,ef3,color='r',  marker='^')
    p31=plt.plot(t,ef4,color='g',marker='o')
      
    plt.xlabel('y',fontsize=12)
    plt.ylabel('EMT output',fontsize=12)
    plt.legend(['EMT 1','EMT 2', 'EMT 3','EMT 4'], loc=0,bbox_to_anchor=(0.55, 0.77))
    plt.title('EMT functions (n={}, x={}, b={})'.format(n, x,b),fontsize=12)
    plt.show()


# Demonstration 2 of four typical EMT instances for 8-bit keys
def test2():
    ef=EmtFunctions(8)
    n=8
    nn=pow(2,n)
    x=292% nn
    b=33% nn

    ef1=[]
    ef2=[]
    ef3=[]
    ef4=[]
    for i in range(nn):
        y=i
        ef1.append(ef.xorb(x,y,b))
        ef2.append(ef.addb(x,y,b))
        ef3.append(ef.xoraddb(x,y,b))
        ef4.append(ef.addxorb(x,y,b))

        #print(i,ef.xorb(x,y,b),ef.addb(x,y,b),ef.xoraddb(x,y,b),ef.addxorb(x,y,b))
    print('n:{},x:{},b:{}'.format(8,x,b))
    plt.figure()
    t=range(nn)
    p21=plt.plot(t,ef1,color='b',  marker='*')
    p22=plt.plot(t,ef2,color='y',  marker='v')
    p23=plt.plot(t,ef3,color='r',  marker='^')
    p31=plt.plot(t,ef4,color='g',marker='o')
      
    plt.xlabel('y',fontsize=12)
    plt.ylabel('EMT output',fontsize=12)
    plt.legend(['EMT 1','EMT 2', 'EMT 3','EMT 4'], loc=0,bbox_to_anchor=(0.55, 0.77))
    plt.title('EMT functions (n={}, x={}, b={})'.format(n, x,b),fontsize=12)
    #plt.xticks(t,t)
    plt.show()

if __name__ == "__main__":
    test1()
    test2()
