# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *

from Vec3d import Vec3d
from Mat3d import Mat3d
import copy

class Shape():
    
    def __init__(self):
        # I am thinking to turn all of them protected
        self.__verticesList = []
        self.__faceList = []
        self.__size = 0

        # I will fix their logic later
        self.__matrix_stack = []
        self.__finalTransformMatrix = 0

        self.__drawer = 0

    def addVertice(self, vx, vy, vz):
        self.__verticesList.append(Vec3d(vx, vy, vz, 1))
        self.__size += 1
        return self
    
    def removeVertice(self, verticeIndex):
        del self.__verticesList[verticeIndex]

    def addFace(self, verticeIndexList):
        self.__faceList.append(verticeIndexList)
    
    def removeFace(self, faceIndex):
        del self.__faceList[faceIndex]

    def addTransformation(self, aMath3d):
        if(len(self.__matrix_stack) == 0):
            self.__finalTransformMatrix = aMath3d
        else:
            self.__finalTransformMatrix = aMath3d.multiplyByMat3d(self.__finalTransformMatrix)
        self.__matrix_stack.append(aMath3d)
        return self
        
    def transformShape(self, aMath3d = 0):
        if(aMath3d == 0):
            aMath3d = self.__finalTransformMatrix
    
        for i in range(self.__size):
            self.__verticesList[i] = aMath3d.multiplyByVec3d(self.__verticesList[i])
        return self
    
    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())
        return self

    def getShape(self):
        return self.__verticesList

    def getFinalTransformationMatrix(self):
        return self.__finalTransformMatrix

    def setFinalTransformationMatrix(self, final):
        self.__finalTransformMatrix = final

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

    # I am not sure to put it to there
    def subdivide(self):
        print("Shape Subdivide")

    def setDrawer(self, drawer):
        self.__drawer = drawer

        self.__drawer.setVerticeList(self.__verticesList)
        self.__drawer.setFaceList(self.__faceList)

    def draw(self):
        self.__drawer.draw()
        
if __name__ == "__main__":
    a = Shape()
    a.addVertice(1,2,3)
    a.addVertice(1,4,6)

    b = Mat3d()
    b.defineRotationMatrix(30,"Z")

    a.transformShape(b)

    print(a)