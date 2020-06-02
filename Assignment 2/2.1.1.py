class ParentSize:

    def __init__(self):
        userList = []
        while True:
            userList = (input("Enter the 3 sides for area of Triangle ").split())
            if(len(userList)==3):
                break
            else:
                print("Try again   ")
        return userList

class Triangle(ParentSize):

    def setup(self,sides):
        self.sides = sides 
    
    def __init__(self):
        dataList  =  ParentSize.__init__(self)
        self.setup(dataList)
    
     

    def get_area(self):
        a, b, c = self.sides
        s = (int(a) + int(b) + int(c)) / 2
        return str((s*(s-int(a))*(s-int(b))*(s-int(c))) ** 0.5)

t = Triangle()
print(" Area of Triangle   ",t.get_area())


