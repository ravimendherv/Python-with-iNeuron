def myfunction(userList):
    tempList = []
    for i in range(len(userList)):
        tempList.append(len(userList[i])) 
    return tempList

userList = list(input("Enter the List of words ").split())
print("The Maps list is  ",myfunction(userList))