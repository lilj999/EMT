import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import emtrate as erate

class EmtProbability(object):

    # To calculate allowed key exposure probability without using EMT, given secret outage probability (s) to be expected.
    def exposure(self,s,m):
        a=1- pow(1-s,1/m)
        exposure=a
        return exposure

    # To calculate allowed key exposure probability with using EMT, given secret outage probability (s) to be expected.
    def exposureemt(self,s,m,w):
        a=1- pow(1-s,1/m)
        exposure=pow(a,1/w)
        return exposure
    
    # To calculate allowed key exposure probability without using EMT, by varing secret outage probability (s) to be expected
    def batch(self, m):
        t=[]
        ls=[]
        for i in range(1,7):
            s=pow(10,-i)
            expo=self.exposure(s,m)
            t.append(s)
            ls.append(expo)
        return t, ls

    # To calculate allowed key exposure probability with using EMT, by varing secret outage probability (s) to be expected
    def batchemt(self, m,w):
        t=[]
        ls=[]
        for i in range(1,7):
            s=pow(10,-i)
            expo=self.exposureemt(s,m,w)
            t.append(s)
            ls.append(expo)
            #print('EmtProb p={},{},{}  expo:{}'.format(s,m,w,expo))
        return t, ls

    # To validating the correctness by reversing the calculation
    def valid(self):
        print('ew',self.exposure(0.1,30))
        print('emt1',self.exposureemt(0.1,30,1))
        print('emt5',self.exposureemt(0.1,30,5))
        ep0=self.exposure(0.1,30)
        ep1=self.exposureemt(0.1,30,1)
        ep2=self.exposureemt(0.1,30,5)

        et=erate.EmtRate()
        print('wl0',et.wholeLoss(ep0,30,1))
        print('wl1',et.wholeLoss(ep1,30,1))
        print('wl5',et.wholeLoss(ep2,30,5))

if __name__ == "__main__":
    # ep=EmtProbability()
    # valid()
    
    ep=EmtProbability()
    t01,zs1=ep.batch(30)
    t02,zs2=ep.batch(60)
    t11,ls11=ep.batchemt(30,5)
    t12,ls12=ep.batchemt(60,5)
    t21,ls21=ep.batchemt(30,10)
    t22,ls22=ep.batchemt(60,10)
    
    # t21,ls21=ep.batchemt(30,10)
    # t22,ls22=ep.batchemt(60,10)
    # t23,ls23=ep.batchemt(90,10)
    
    fig1, ax1 = plt.subplots()
    #plt.figure()
    p21=ax1.plot(t01,zs1,color='r', linestyle='--', marker='o')
    p22=ax1.plot(t02,zs2,color='r',  marker='+')
    #p23=ax1.plot(t11,ls11,color='r', linestyle='dotted', marker='^')
    p23=ax1.plot(t11,ls11,color='y',linestyle='--', marker='o')
    p31=ax1.plot(t12,ls12,color='y',marker='+')
    p32=ax1.plot(t21,ls21,color='b',linestyle='--',marker='o')
    p33=ax1.plot(t22,ls22,color='b',marker='+')

    print('SOP without EMT, m=30',t01,zs1)
    print('SOP with EMT, m=30, w=5',t11,ls11)
    print('SOP with EMT, m=30, w=10',t21,ls21)
    print('SOP without EMT, m=60',t02,zs2)
    print('SOP with EMT, m=60, w=5',t12,ls12)
    print('SOP with EMT, m=60, w=10',t22,ls22)
   
    ax1.set_xlabel('Secret outage probability (SOP)',fontsize=12)
    ax1.set_ylabel('Allowed key exposure probability (p)',fontsize=12)
    ax1.set_xscale("log")
    ax1.set_xlim(5e-7, 2e-1)
    ax1.set_yscale("log")
    ax1.set_ylim(6e-9, 2e0)
    # for a, b in zip(t12, ls12):
    #     plt.text(a, b, '{:.2f}'.format(b), ha='center', va='top', fontsize=12)

    for a, b in zip(t22, ls22):
        plt.text(a, b, '{:.2f}'.format(b), ha='center', va='bottom', fontsize=12)


    ax1.legend(['Non-EMT m=30','Non-EMT m=60', 'EMT m=30, w=5','EMT m=60, w=5','EMT m=30, w=10', 'EMT m=60, w=10'], loc=0,bbox_to_anchor=(0.55, 0.77))
    ax1.set_xticks(t01,t01)
    plt.show()

