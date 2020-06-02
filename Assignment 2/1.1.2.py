def myfilter(negative_value_in_list, ip_list):

 result = []
 for i in ip_list:
  if negative_value_in_list(i):
   result.append(int(i))

 return result



def negative_value_in_list(x):
 if (int(x) <= 0): 
  return x 

userList = list(input("Enter the Interger List ").split())
print ("Negative No Output is "  + str(myfilter(negative_value_in_list, userList)))
