from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Cylinder(Shape):

    def __init__(self):
        Shape.__init__(self)
        self.__quadLength = 0.83 * 2
        self.defineRectangle(self, self.__quadLength / 2.0)

    # Exactly same with Box method I will refactor later
    def calculateScanAngle(self, distance):
        # Distance is how far the quad from center
        # Calculate angle to rotate for a quad to match one edge
        # 0.83 will be extracted to a variable later it done this way because it should be multiple of circle round I guess
        hipotenous = math.sqrt((distance * distance) + (self.__quadLength / 2 * self.__quadLength / 2))
        half_angle_radian = math.acos(distance / float(hipotenous))
        angle = 2 * (half_angle_radian * 180 / math.pi)
        return angle

    def defineRectangle(self,shape, length):
        # Start from right top and continue counter clockwise
        shape.addVertice(length,length,0)
        shape.addVertice(-length,length,0)
        shape.addVertice(-length ,-length,0)
        shape.addVertice(length,-length,0)

    def drawCylinder(self):
        distance = 2
        angle = self.calculateScanAngle(distance)
        rotateNum = 360.0 / angle
    
        self.transformShape(Mat3d().defineTranslationMatrix(0,0,distance))
        
        for i in range(int(rotateNum)):
            tmp = self.clone()
            tmp.transformShape(Mat3d().defineRotationMatrix(angle, "Y"))
            self.addVerticesOfShape(tmp)

        self.transformShape(Mat3d().defineScalingMatrix(1,3,1))

    def subdivide(self, round):
        # I will improve it later
        step = self.__quadLength / float(2 ** round)
        
        self.resetShape()
        self.defineRectangle(self, step / 2)
      
        if(round != 0):
            self.transformShape(Mat3d().defineTranslationMatrix((step / 2.0) - (self.__quadLength / 2.0) , 0, 0))

        tmp = self.clone()
        for i in range(2 ** round - 1):
            tmp.transformShape(Mat3d().defineTranslationMatrix(step, 0, 0))
            self.addVerticesOfShape(tmp)
        
        self.drawCylinder()
        

    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())
 
    def __str__(self):
        return Shape.__str__(self)
        
    
