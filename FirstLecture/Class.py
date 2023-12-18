class Student:
    def __init__(self, name, age, height):
        self.__name = name #set private (encapsulation)
        self.age = age
        self.height = height 
    def getName(self):
        return self.__name
    def setName(self,value):
        self.__name = value
class TienPhan(Student):
    def __init__(self, name, age, height, hobby):
        super().__init__(name, age, height)
        self.hobby = hobby
    def Study(self):
        pass
    def Sport(self):
        print('Basketball')

class JohnCena(Student):
    def Study(self):
        pass
    def Sport(self):
        print('Wrestling')
pnt = TienPhan('Phan Ngoc Tien',21, 173, 'Fucking')
print(pnt.hobby)
# print(pnt.name) # luc nay chua dung tinh dong goi
pnt.Sport()

jcn = JohnCena('John Cena', 36, 187)

#polynoshism
pnt.Sport()
jcn.Sport()

#encapsulation
#print(pnt.__name) ### extract error
print(pnt.getName())

    