def filter_long_words(userList,userVal):
    tempList = []
    for i in range(len(userList)):
        if (len(userList[i]) > userVal):
            tempList.append(userList[i]) 
    return tempList

userList = list(input("Enter the List of words ").split())
userVal = int(input("Enter the Integer Value  "))
print("The list is who have longest string length than ",userVal," is  ",filter_long_words(userList,userVal))