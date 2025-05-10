import random
import numpy as np

M=10

#Random points p_i IID and uniform on (0,1000]
def randp_i():
    a=random.uniform(0, 1000)
    b=random.uniform(0, 1000)
    c=random.uniform(0, 1000)
    while a==b or a==c or c==b or a==0 or b==0 or c==0:
        a=random.uniform(1, 1000)
        b=random.uniform(1, 1000)
        c=random.uniform(1, 1000)
    return(np.asarray([a,b,c]))
print(randp_i())

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
    A=randp_i()
    appt=app(A[0], A[1], A[2], M)
    SD=(A[0]+ A[1]+ A[2])/M
    LQ = np.floor(A/SD)
    if appt[0]<LQ[0] or appt[1]<LQ[1] or appt[2]<LQ[2]:
        qvio=qvio+1
    else:
        qpass=qpass+1

print(qvio/(qvio+qpass))