import numpy as np

#Defining Divsor function

def divisor_funct (X):
     #return np.sqrt(X*(X+1)) #Huntington-Hill
     #return X #Adams
     return X+1 #Jefferson's
     #return (2*X*(X+1))/(2*X +1) #Dean's

#Picking M 
M=3

#Defining vertices:
def P_1(a,b):
     H=M-a-b
     U_1=H*(divisor_funct(a))
     U_2=a*(divisor_funct(H-1))
     U_3=divisor_funct(a)
     L=divisor_funct(H-1)
     return (U_1-U_2-U_3)/L

def X_1(a,b):
     return min(P_1(a,b), 1-P_1(b,a))

def X_2(a,b):
     return max(P_1(a,b), 1-P_1(b,a))

def Y_1(a,b):
     return 1-X_1(a,b)

def Y_2(a,b):
     return 1 - X_2(a,b)

def Y_3(a,b):
     H=M-a-b
     U_1=H*(divisor_funct(b))
     U_2=b*(divisor_funct(H-1))
     U_3=b*(divisor_funct(a))
     U_4=a*(divisor_funct(b))
     L= (divisor_funct(H-1)) + (divisor_funct(a))+(divisor_funct(b))
     return (U_1-U_2-U_3+U_4)/L

def X_3(a,b):
     return Y_3(b,a)

#Defining Area
def Areafunc (a,b):
     E_1=(X_1(a,b))*(Y_2(a,b)-Y_3(a,b))
     E_2= (Y_1(a,b)) *(X_2(a,b)-X_3(a,b))
     E_3 = (X_2(a,b))*(Y_3(a,b)) - (X_3(a,b))*(Y_2(a,b))
     AA = 0.5*(E_1 - E_2 + E_3)
     return max(0, AA)

#Calculating Prob
TotalArea = 0


for i in range (0,round(np.ceil((M/2)))):
     if i <= M/3:
          Top=round(np.floor(-(i/2)+(M/2)-0.5))
     if i > (M/3) :
          Top=round(np.floor( -(2*i)+M-0.5   ))
     for j in range (0, Top+1):
          TotalArea=TotalArea+Areafunc(i,j)
print("Theoretical Prob is:", (6/(M*M))*TotalArea)