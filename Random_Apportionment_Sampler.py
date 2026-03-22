import random
import numpy as np

#Pick M
M=5

#defining divisor function
def divisor_funct (X):
     #return np.sqrt(X*(X+1)) #Huntington-Hill
     return X #Adams
     #return (2*X*(X+1))/(2*X +1) #Dean's
     #return X+1 #Jeffersons
     

#define random populations

alpha = 2  #Dirichlet Distribution Paramater
beta = 1  #Exponential Distribution Paramater
a_0 = 0   #Parameter for uniform (a_0, b_0)
b_0 = 1000   #Parameter for uniform (a_0, b_0)
def randpops(m):
     #return [random.uniform(a_0,b_0),random.uniform(a_0,b_0),random.uniform(a_0,b_0)]   #p_i IID, uniform (0,1000)
     return m*np.random.dirichlet([alpha,alpha,alpha])                                         #q_i dirichlet
     #return [1*np.random.exponential(beta),np.random.exponential(beta),np.random.exponential(beta) ]    #p_i IID, exponential

#Defining the apportionment
def app_0 (R,A,B, m):             #for d(0)=0 i.e. not jefferson
    Rb=1
    Ab=1
    Bb=1
    pop=np.asarray([R,A,B])
    for i in range(0, m-3):
        seats=np.asarray([Rb,Ab,Bb])
        Pri = pop/divisor_funct(seats)
        if Pri[0]==Pri.max():
            Rb=Rb+1
        if Pri[1]==Pri.max():
            Ab=Ab+1
        if Pri[2]==Pri.max():
            Bb=Bb+1
    return np.asarray([Rb,Ab,Bb])

def app_n0 (R,A,B, m):             #for d(0) not 0
    Rb=0
    Ab=0
    Bb=0
    pop=np.asarray([R,A,B])
    for i in range(0, m):
        seats=np.asarray([Rb,Ab,Bb])
        Pri = pop/divisor_funct(seats)
        if Pri[0]==Pri.max():
            Rb=Rb+1
        if Pri[1]==Pri.max():
            Ab=Ab+1
        if Pri[2]==Pri.max():
            Bb=Bb+1
    return np.asarray([Rb,Ab,Bb])
def app(R,A,B,m):
     if divisor_funct (0) == 0:
         return app_0 (R,A,B, m)
     if divisor_funct (0) > 0 :
         return app_n0 (R,A,B, m)
     

#Running sample:
qpass=0
qvio=0

trials=100000

for i in range(0, trials):
    A=randpops(M)
    appt=app(A[0], A[1], A[2], M)
    P=A[0]+A[1]+A[2]
    Quotas= np.asarray([(M/P)*A[0],(M/P)*A[1], (M/P)*A[2] ])
    LQ = np.asarray([np.floor( Quotas[0]), np.floor( Quotas[1]), np.floor( Quotas[2]) ])
    UQ =np.asarray([np.ceil( Quotas[0]), np.ceil( Quotas[1]), np.ceil( Quotas[2]) ])
    if appt[0]<LQ[0] or appt[1]<LQ[1] or appt[2]<LQ[2] or appt[0]>UQ[0] or appt[1]>UQ[1] or appt[2]>UQ[2]:
        qvio=qvio+1
    else:
        qpass=qpass+1

#Sample Conclusions:
Prob=qvio/(qvio+qpass)

#(note for confidence interval number of trials must be large to be accurate)

err = 1.96*(np.sqrt( (Prob*(1-Prob))/(trials)   ))

print("Sample probability is", Prob)
print("Confidence interval is:", "(", Prob-err, ",", Prob+err, ")")