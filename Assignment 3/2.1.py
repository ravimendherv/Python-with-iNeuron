import numpy as np
   
def myMatrixFunction(pVector, n, booleanValueIn):
    
    if not booleanValueIn:
        temp = []
        for x in pVector:
            for i in range(n):
                temp.append(x**(n-1-i))
        giveBack = np.array(temp).reshape(pVector.size,n)

    elif booleanValueIn:
        temp = []
        for x in pVector:
            for i in range(n):
                temp.append(x**i)
        giveBack = np.array(temp).reshape(pVector.size,n)
    
    return giveBack


temp = list(input("Enter the Interger List  ").split())
temp = list(map(int, temp))
userVector = np.array(temp)
noOfColumn = int(input("Enter the Numbers of Columns  "))
while True:
    booleanValue = int(input("Enter 0 for false boolean value \n Enter 1 for ture boolean value.\n Please Enter your choice  "))
    print("The input array is:",userVector,"\n")
    if booleanValue==0:
        falseVector = myMatrixFunction(userVector,noOfColumn,False)
        print("The Boolean value is FALSE  Hence Matrix is \n\n",falseVector,"\n")
        break
    elif booleanValue==1:
        tureVector = myMatrixFunction(userVector,noOfColumn,True)
        print("The Boolean value is TRUE  Hence Matrix is \n\n",tureVector,"\n")
        break
