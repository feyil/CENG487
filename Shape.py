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
        self.__verticesList = []
        self.__size = 0

        self.__matrix_stack = []
        self.__finalTransformMatrix = 0

        # OpenGL related
        self.__drawAs = 0
        # End

    def addVertice(self, vx, vy, vz):
        self.__verticesList.append(Vec3d(vx, vy, vz, 1))
        self.__size += 1
        return self

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

    # OpenGL related code
    def drawAs(self, drawAs):
        self.__drawAs = drawAs

    def drawGL(self):
        #glTranslate(0,0,-6)
        glBegin(self.__drawAs)
        color = 0
        for i in self.getShape():
		    color += 1
		    if(color % 2 == 0):
			    glColor3f(0.8, 0.3, 0.8)
		    else:
			    glColor3f(0.2, 0.8, 0.3)
		    glVertex3f(i.getX(), i.getY(), i.getZ())
        glEnd() 
    # End
            
        
if __name__ == "__main__":
    a = Shape()
    a.addVertice(1,2,3)
    a.addVertice(1,4,6)

    b = Mat3d()
    b.defineRotationMatrix(30,"Z")

    a.transformShape(b)

    print(a)