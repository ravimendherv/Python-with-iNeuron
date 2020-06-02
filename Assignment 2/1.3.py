def longestWord(userList):
    largest = 0
    for i in range(len(userList)):
        if(len(str(userList[i]))>largest):
            largest= len(str(userList[i]))
    return largest

userList = list(input("Enter the List of words   ").split())
print(longestWord(userList))

