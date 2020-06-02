
def myreduce(sum, userList):

  result = int(userList[0])
  for i in userList[1:]:
   result = sum(result, int(i))

  return result




def sum(a,b): return a + b
 
userList = list(input("Enter the Interger List ").split())

print ("Sum of Given list is "   + str(myreduce(sum, userList)))