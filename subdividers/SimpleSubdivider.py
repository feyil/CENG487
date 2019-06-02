from Subdivider import Subdivider, SubdividerType
from utils import Vec3d


class SimpleSubdivider(Subdivider):

    def __init__(self, shape):
        Subdivider.__init__(self, shape)

        self.__subdivisionHistory = []
    
    def subdivide(self, indicator = '+'):
        if(indicator == '+'):
            newFaceList = []

            for face in self.getShape().getFaceList():
                newFaceList += self.__subdivideFace(face)
                
            self.__subdivisionHistory.append(self.getShape().getFaceList())
   
            self.getShape().setFaceList(newFaceList)
        elif(indicator == '-'):
            if(len(self.__subdivisionHistory) != 0):
                self.getShape().setFaceList(self.__subdivisionHistory.pop())
        
    def __subdivideFace(self, quadFace):
        index = self.getShape().getSize()
        xCenter = Vec3d(0,0,0,0)
        for verticeIndex in quadFace:
            xCenter.addVec3d(self.getShape().getVerticeList()[verticeIndex])
        xCenter.scalarMultiplication(0.25)
        self.getShape().getVerticeList().append(xCenter)
        xCenterIndex = index

        x1 = Vec3d(0,0,0,0)
        x1.addVec3d(self.getShape().getVerticeList()[quadFace[0]]).addVec3d(self.getShape().getVerticeList()[quadFace[1]]).scalarMultiplication(0.5)
        self.getShape().getVerticeList().append(x1)
        x1Index = index + 1

        x2 = Vec3d(0,0,0,0)
        x2.addVec3d(self.getShape().getVerticeList()[quadFace[1]]).addVec3d(self.getShape().getVerticeList()[quadFace[2]]).scalarMultiplication(0.5)
        self.getShape().getVerticeList().append(x2)
        x2Index = index + 2

        x3 = Vec3d(0,0,0,0)
        x3.addVec3d(self.getShape().getVerticeList()[quadFace[2]]).addVec3d(self.getShape().getVerticeList()[quadFace[3]]).scalarMultiplication(0.5)
        self.getShape().getVerticeList().append(x3)
        x3Index = index + 3

        x4 = Vec3d(0,0,0,0)
        x4.addVec3d(self.getShape().getVerticeList()[quadFace[0]]).addVec3d(self.getShape().getVerticeList()[quadFace[3]]).scalarMultiplication(0.5)
        self.getShape().getVerticeList().append(x4)
        x4Index = index + 4
        
        self.getShape().setSize(self.getShape().getSize() + 5)

        faceList = [[x1Index, quadFace[1], x2Index, xCenterIndex],
                    [x2Index, quadFace[2], x3Index, xCenterIndex],
                    [x3Index, quadFace[3], x4Index, xCenterIndex],
                    [x4Index, quadFace[0], x1Index, xCenterIndex]]
        
        return faceList
        