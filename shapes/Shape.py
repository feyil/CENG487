# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import *

import copy

from drawers.Drawer import *
from utils import Vec3d, Mat3d, ColorRGBA
from subdividers import SimpleSubdivider, SubdividerType, CatmullClarkSubdivider

class Shape:
    
    def __init__(self):
        self.__shapeName = ""
    
        # I am thinking to turn all of them protected
        self.__verticesList = []
        self.__faceList = []
        self.__size = 0

        # I will fix their logic later
        self.__matrix_stack = []
        self.__finalTransformMatrix = 0

        self.__drawer = 0

        self.__subdivider = None

        self.__color = None
        self.__wireColor = None
        self.__wireWidth = None

    def setColor(self, r, g, b, a):
        self.__color = ColorRGBA(r, g, b, a)

    def setWireColor(self, r, g, b, a):
        self.__wireColor = ColorRGBA(r, g, b, a)

    def setWireWidth(self, width):
        self.__wireWidth = width

    def setShapeName(self, shapeName):
        self.__shapeName = shapeName

    def getShapeName(self):
        return self.__shapeName
    
    def getShape(self):
        return self.__verticesList

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

    def setVerticeList(self, verticeList):
        self.__verticesList = verticeList

    def getVerticeList(self):
        return self.__verticesList

    def setFaceList(self, faceList):
        self.__faceList = faceList
    
    def getFaceList(self):
        return self.__faceList

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size
    
    def getFinalTransformationMatrix(self):
        return self.__finalTransformMatrix

    def setFinalTransformationMatrix(self, final):
        self.__finalTransformMatrix = final

    def resetShape(self):
        self.__verticesList = []
        self.__size = 0
        return self

    def subdivide(self, indicator = '+'):
        if(self.__subdivider != None):
            self.__subdivider.subdivide(indicator)
    
    def setSubdivider(self, subdividerType):    
        if(subdividerType == SubdividerType.SIMPLE_SUBDIVIDER):
            self.__subdivider = SimpleSubdivider(self)
        elif(subdividerType == SubdividerType.CATMULL_CLARK_SUBDIVIDER):
            self.__subdivider = CatmullClarkSubdivider(self)
        else:
            pass

    def setDrawer(self, drawer):
        self.__drawer = drawer
        self.setDrawStyle()
    
    def setDrawStyle(self, drawStyle = DrawStyle.NODRAW):
        self.__drawer.setDrawStyle(drawStyle)
    
    def draw(self):
        drawer = self.__drawer
        
        # give the shape to drawer
        drawer.setVerticeList(self.__verticesList)
        drawer.setFaceList(self.__faceList)

        # Coloring
        drawer.setColor(self.__color)
        drawer.setWireColor(self.__wireColor)
        drawer.setWireWidth(self.__wireWidth)

        # Fire the drawer
        drawer.draw()

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        output = ""
        for i in self.__verticesList:
            output += i.__str__() + "\n"
        output += "Face List: \n"
        output += self.__faceList.__str__() + "\n"
        return output
        
if __name__ == "__main__":
    a = Shape()
    a.addVertice(1,2,3)
    a.addVertice(1,4,6)

    b = Mat3d()
    b.defineRotationMatrix(30,"Z")

    a.transformShape(b)

    print(a)