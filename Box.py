from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Box(Shape):

    def __init__(self):
        Shape.__init__(self)
        self.__quadLength = 2
        self.defineQuad(self, self.__quadLength / 2.0)

    def calculateScanAngle(self, distance):
        # Distance is how far the quad from center
        # Calculate angle to rotate for a quad to match one edge
        hipotenous = math.sqrt((distance * distance) + 1)
        half_angle_radian = math.acos(distance / hipotenous)
        angle = 2 * (half_angle_radian * 180 / math.pi)
        return angle

    def defineQuad(self,shape, length):
        # Start from right top and continue counter clockwise
        shape.addVertice(length,length,0)
        shape.addVertice(-length,length,0)
        shape.addVertice(-length,-length,0)
        shape.addVertice(length,-length,0)

    def drawBox(self):
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

    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())

    def subdivide(self, round):
        # I will improve it later
        # Idea of Cylinder draw can be applied here may be
        # Clone probably slow down the process significantly
        step = self.__quadLength / float(2 ** round)
        
        self.resetShape()
        self.defineQuad(self, step / 2)
      
        if(round != 0):
            self.transformShape(Mat3d().defineTranslationMatrix((step / 2.0) - (self.__quadLength / 2.0) , 0, 0))

        tmp = self.clone()
        for i in range(2 ** round - 1):
            tmp.transformShape(Mat3d().defineTranslationMatrix(step, 0, 0))
            self.addVerticesOfShape(tmp)
        
        if(round != 0):
            self.transformShape(Mat3d().defineTranslationMatrix(0, self.__quadLength / 2.0 - (step / 2.0), 0))
           
        tmp = self.clone()
        for j in range(2 ** round - 1):
            tmp.transformShape(Mat3d().defineTranslationMatrix(0,-step,0))
            self.addVerticesOfShape(tmp)
        
        self.drawBox()

    def __str__(self):
        return Shape.__str__(self)


if __name__ == "__main__":
    a = Box()
    a.drawBox()
    print(a)