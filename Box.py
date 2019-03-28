# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from Primitives3D import Primitive3D

from Mat3d import Mat3d
from Vec3d import Vec3d

class Box(Primitive3D):

    def __init__(self):
        Primitive3D.__init__(self)
        self.__quadLength = 2
        self.defineQuad(self, self.__quadLength / 2.0)

    def createBox(self):
        distance = 1
        angle = self.calculateScanAngle(distance)
        
        # Quad with 180 degree rotated side by side
        temp = self.transformShape(Mat3d().defineTranslationMatrix(0,0,distance)).clone()
        temp.transformShape(Mat3d().defineRotationMatrix(angle * 2, "Y"))
        self.addVerticesOfShape(temp)

        # Side by side quad rotated around Y
        scanShape = self.clone().transformShape(Mat3d().defineRotationMatrix(angle, "Y"))
        self.addVerticesOfShape(scanShape)
        
        # Side by side quad rotated aroun Z
        scanShape.transformShape(Mat3d().defineRotationMatrix(angle, "Z"))
        self.addVerticesOfShape(scanShape)

    def draw(self, division = 0):
        # I will improve it later
        # Idea of Cylinder draw can be applied here may be
        # Clone probably slow down the process significantly
        step = self.__quadLength / float(2 ** division)
        
        self.resetShape()
        self.defineQuad(self, step / 2)
      
        if(division != 0):
            self.transformShape(Mat3d().defineTranslationMatrix((step / 2.0) - (self.__quadLength / 2.0) , 0, 0))

        tmp = self.clone()
        for i in range(2 ** division - 1):
            tmp.transformShape(Mat3d().defineTranslationMatrix(step, 0, 0))
            self.addVerticesOfShape(tmp)
        
        if(division != 0):
            self.transformShape(Mat3d().defineTranslationMatrix(0, self.__quadLength / 2.0 - (step / 2.0), 0))
           
        tmp = self.clone()
        for j in range(2 ** division - 1):
            tmp.transformShape(Mat3d().defineTranslationMatrix(0,-step,0))
            self.addVerticesOfShape(tmp)
        
        self.createBox()

    def __str__(self):
        return Primitive3D.__str__(self)


if __name__ == "__main__":
    print("Hello")