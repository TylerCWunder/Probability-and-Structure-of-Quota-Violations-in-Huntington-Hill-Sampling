import random
import numpy as np

M=10

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

#Defining Huntington-Hill
def app (R,A,B, m):
    Rb=1
    Ab=1
    Bb=1
    pop=np.asarray([R,A,B])
    for i in range(0, m-3):
        seats=np.asarray([Rb,Ab,Bb])
        Pri = pop/np.sqrt(seats*(seats+1))
        if Pri[0]==Pri.max():
            Rb=Rb+1
        if Pri[1]==Pri.max():
            Ab=Ab+1
        if Pri[2]==Pri.max():
            Bb=Bb+1
    return np.asarray([Rb,Ab,Bb])

#Creating sample and counting violations
qpass=0
qvio=0

trials=100000

for i in range(0, trials):
    A=randq_1q_2(M)
    appt=app(A[0], A[1], M-A[0] - A[1], M)
    LQ = np.asarray([np.floor(A[0]),np.floor(A[1]), np.floor(M-A[0] - A[1]) ])
    if appt[0]<LQ[0] or appt[1]<LQ[1] or appt[2]<LQ[2]:
        qvio=qvio+1
    else:
        qpass=qpass+1

print(qvio/(qvio+qpass))