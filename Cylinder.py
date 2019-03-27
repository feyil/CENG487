from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Cylinder(Shape):

    def __init__(self):
        Shape.__init__(self)
        self.__quadLength = 0.83 * 2
    
    def drawCylinder(self, r = 1, length = 3, scanAngle = 5):
        step = scanAngle
        
        # (360 mod scanAngle) assumed 0
        while(step <= 360):
            # Rotating around y axis 
            a,b = self.calculatePolarCoordinate(r, step)
            step += scanAngle 
            c,d = self.calculatePolarCoordinate(r, step)

            self.addVertice(a,length / 2.0,b)
            self.addVertice(c,length / 2.0,d)
            self.addVertice(c,-length / 2.0,d)
            self.addVertice(a,-length / 2.0,b)

    def calculateRadian(self, degree):
        return degree * (math.pi / 180)   
    
    def calculatePolarCoordinate(self, r, degree):
        radian = self.calculateRadian(degree)
        a = r * math.cos(radian)
        b = r * math.sin(radian)
        return a, b
    
    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())
 
    def __str__(self):
        return Shape.__str__(self)
        
    
