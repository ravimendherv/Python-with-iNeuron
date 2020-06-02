ip = "ACADGILD"
outputList = [ i for i in ip ]
# outputList = []
# for i in ip:
#     outputList.append(i)
print (outputList)

ip1 = ['x','y','z']
outputList1 = [ i*n for i in ip1 for n in range(1,5)  ]
# outputList1=[]
# for i in ip1:
#     for n in range(1,5):
#         outputList1.append(i*n)
print(outputList1)

ip2 = ['x','y','z']
outputList2 = [ i*n for n in range(1,5) for i in ip2 ]
# outputList2=[]
# for n in range(1,5):
#     for i in ip2:
#         outputList2.append(i*n)
print(outputList2)

ip3 = [2,3,4]
outputList3 = [ [i+n] for i in ip3 for n in range(0,3)]
# outputList3=[]
# for i in ip3:
#     for n in range(0,3):
#         outputList3.append([i+n])
print(outputList3)

ip4 = [2,3,4,5]
outputList4 = [ [i+n for i in ip4] for n in range(0,4)  ]
print(outputList4)

ip5=[1,2,3]
outputList5 = [ (b,a) for a in ip5 for b in ip5]
print(outputList5)
