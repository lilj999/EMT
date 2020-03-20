import math
import emtfunction as ef
import numpy as np

class EmtEntropy(object):

    def __init__(self, n):
        self.n=n
        self.nn=pow(2,n)
        self.emtf=ef.EmtFunctions(self.n)

    # To calculate Shannon entropy for a distribution with probabilities p_1,p_2,...,p_nn.
    def entropy(self, lstProp):
        assert(len(lstProp)==self.nn)
        en=0
        for p in lstProp:
            en=en- math.log(p,2)*p
        return en

    # To calculate min-entropy for a distribution with probabilities p_1,p_2,...,p_nn.
    def min_entropy(self, lstProp):
        assert(len(lstProp)==self.nn)
        en=0
        mp=0
        for p in lstProp:
            if mp< p:
                mp=p
        en=  -math.log(mp,2)
        return en
    
    # To calculate the distribution of probabilities after performing EMT_xorb on X and Y
    def xor_prob(self, X, Y,b):
        assert(len(X)==self.nn)
        assert(len(Y)==self.nn)
        
        zp=np.zeros(self.nn)
        for xi in range(self.nn):
            for yi in range(self.nn):
                zi= self.emtf.xorb(xi,yi,b)
                zp[zi]=zp[zi]+ X[xi]*Y[yi]
          
        return zp 

    # To calculate the distribution of probabilities after performing EMT_addb on X and Y
    def add_prob(self, X, Y,b):
        assert(len(X)==self.nn)
        assert(len(Y)==self.nn)
        
        zp=np.zeros(self.nn)
        for xi in range(self.nn):
            for yi in range(self.nn):
                zi= self.emtf.addb(xi,yi,b)
                zp[zi]=zp[zi]+ X[xi]*Y[yi]
          
        return zp 

    # To calculate the distribution of probabilities after performing EMT_xoraddb on X and Y
    def xoradd_prob(self, X, Y,b):
        assert(len(X)==self.nn)
        assert(len(Y)==self.nn)
        
        zp=np.zeros(self.nn)
        for xi in range(self.nn):
            for yi in range(self.nn):
                zi= self.emtf.xoraddb(xi,yi,b)
                zp[zi]=zp[zi]+ X[xi]*Y[yi]
          
        return zp 

    # To calculate the distribution of probabilities after performing EMT_addxorb on X and Y
    def addxor_prob(self, X, Y,b):
        assert(len(X)==self.nn)
        assert(len(Y)==self.nn)
        
        zp=np.zeros(self.nn)
        for xi in range(self.nn):
            for yi in range(self.nn):
                zi= self.emtf.addxorb(xi,yi,b)
                zp[zi]=zp[zi]+ X[xi]*Y[yi]
          
        return zp 

    def printResult(self,prefix,X,value):
        str=prefix+'['
        for x in X:
            str=str+ '{:.2f},'.format(x)
        str=str+'] {:.2f}'.format(value) 
        print(str)
        return str


if __name__ == "__main__":
    pass

emt=EmtEntropy(2)

#X=[1/4,1/4,1/4,1/4]
X=[1/2,1/4,1/8,1/8]
Y=[1/5,2/5,1/5,1/5]
Z=[1/7,3/7,2/7,1/7]
    
emt.printResult('entropy X', X, emt.entropy(X))
emt.printResult('minentropy X', X, emt.min_entropy(X))
emt.printResult('entropy Y', Y, emt.entropy(Y))
emt.printResult('minentropy Y', Y, emt.min_entropy(Y))
emt.printResult('entropy Z', Z, emt.entropy(Z))
emt.printResult('minentropy Z', Z, emt.min_entropy(Z))

U= emt.addxor_prob(X,Y,0)
emt.printResult('entropy addxor0_u',U, emt.entropy(U))
emt.printResult('minentropy addxor0_u',U, emt.min_entropy(U))

xor0= emt.xor_prob(U,Z,0)
emt.printResult('\nentropy xor0_k1',xor0, emt.entropy(xor0))
emt.printResult('minentropy xor0_k1',xor0, emt.min_entropy(xor0))
xor1= emt.xor_prob(U,Z,1)
emt.printResult('entropy xor1_k2',xor1, emt.entropy(xor1))
emt.printResult('minentropy xor1_k2',xor1, emt.min_entropy(xor1))
add0= emt.add_prob(U,Z,0)
emt.printResult('entropy add0_k3',add0, emt.entropy(add0))
emt.printResult('minentropy add0_k3',add0, emt.min_entropy(add0))

