# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from Vec3d import Vec3d
from Mat3d import Mat3d
import copy

class Shape():
    
    def __init__(self):
        self.__verticesList = []
        self.__size = 0
        self.__matrix_stack = []
        self.__order = []

    def addVertice(self, vx, vy, vz):
        self.__verticesList.append(Vec3d(vx, vy, vz, 1))
        self.__size += 1
        return self
        
    def transformShape(self, aMath3d):
        for i in range(self.__size):
            self.__verticesList[i] = aMath3d.multiplyByVec3d(self.__verticesList[i])
        return self
    
    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())

    def getShape(self):
        return self.__verticesList

    def resetShape(self):
        self.__verticesList = []
        self.__size = 0
        return self

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        output = ""
        for i in self.__verticesList:
            output += i.__str__() + "\n"
        return output
            
        
if __name__ == "__main__":
    a = Shape()
    a.addVertice(1,2,3)
    a.addVertice(1,4,6)

    b = Mat3d()
    b.defineRotationMatrix(30,"Z")

    a.transformShape(b)

    print(a)