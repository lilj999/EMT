import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

class EmtRate(object):

    # To calculate the secret outage probability (SOP) within one EMT window
    def winLoss(self,p,w):
        loss=1-pow(1-pow(p,w),w)
        return loss
    
    # To calculate the secret outage probability (SOP) for a session of length: m
    def wholeLoss(self,p,m,w):
        loss= 1-pow(1-pow(p,w),m)
        return loss

    # To calculate the secret outage probability (SOP) by varing w for given p
    def batch(self, p):
        t=[]
        ls=[]
        for i in range(10):
            w=i+1
            loss=ew.wholeLoss(p,60,w)
            t.append(w)
            ls.append(loss)
            print('EmtRate p={},60,{}'.format(p,w),loss)
        return t, ls

if __name__ == "__main__":
    ew=EmtRate()
    t1,ls1=ew.batch(0.01)
    t2,ls2=ew.batch(0.1)
    t3,ls3=ew.batch(0.5)
    
    zs1=np.ones(10)*ls1[0]
    zs2=np.ones(10)*ls2[0]
    zs3=np.ones(10)*ls2[0]

    plt.figure()
    p21=plt.plot(t1,zs1,color='b', linestyle='--', marker='*')
    p22=plt.plot(t2,zs2,color='y', linestyle='dashdot', marker='v')
    p23=plt.plot(t3,zs3,color='r', linestyle='dotted', marker='^')
    p31=plt.plot(t1,ls1,color='b',marker='o')
    p32=plt.plot(t2,ls2,color='y',marker='o')
    p33=plt.plot(t3,ls3,color='r',marker='o')

    # for a, b in zip(t2, ls2):
    #     plt.text(a, b, '{:.1e}'.format(b), ha='center', va='top', fontsize=12)
   
    plt.xlabel('EMT window size(w)',fontsize=12)
    plt.ylabel('Secret outage probability',fontsize=12)
    plt.legend(['Non-EMT p=0.01','Non-EMT p=0.1', 'Non-EMT p=0.5','EMT p=0.01','EMT p=0.1', 'EMT p=0.5'], loc=0,bbox_to_anchor=(0.55, 0.77))
    plt.xticks(t1,t1)
    plt.show()
