import random
import numpy as np

#Pick M
M=3

#defining divisor function
def divisor_funct (X):
     #return np.sqrt(X*(X+1)) #Huntington-Hill
     #return X #Adams
     return X+1 #Jeffersons
     #return (2*X*(X+1))/(2*X +1) #Adams

#Random Quota Function
def randq_1q_2 (m):
    #Picking random coordinates on the square (0, M/3) x (0, M/2):
    a=random.uniform(0,m/3)
    b=random.uniform(0,m/2)
    while a==0  or a==m/3 or b==0 or b== (m/2) - (1/2)*a or a==b:
        a=random.uniform(0,m/3)
        b=random.uniform(0,m/2)
    #putting the random coordinates onto the desired region by moving points in the top triangle
    if a >= m - a - b or b>= m-a-b:
        q_1= (5/6)*m - b
        q_2= (1/3)*m - a
    if a<m - a - b and b<m-a-b:
        q_1 = a
        q_2=b
    return np.asarray([q_1,q_2])


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




#Creating sample and counting violations
qpass=0
qvio=0

trials=100000

for i in range(0, trials):
    A=randq_1q_2(M)
    appt=app(A[0], A[1], M-A[0] - A[1], M)
    LQ = np.asarray([np.floor(A[0]),np.floor(A[1]), np.floor(M-A[0] - A[1]) ])
    UQ =np.asarray([np.ceil(A[0]),np.ceil(A[1]), np.ceil(M-A[0] - A[1]) ])
    if appt[0]<LQ[0] or appt[1]<LQ[1] or appt[2]<LQ[2] or appt[0]>UQ[0] or appt[1]>UQ[1] or appt[2]>UQ[2]:
        qvio=qvio+1
    else:
        qpass=qpass+1

Prob=qvio/(qvio+qpass)

#confidence interval (number of trials must be large to be accurate)

err = 1.96*(np.sqrt( (Prob*(1-Prob))/(trials)   ))

print("Sample probability is", Prob)
print("Confidence interval is:", "(", Prob-err, ",", Prob+err, ")")
