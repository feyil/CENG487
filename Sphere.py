from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Sphere(Shape):

    def __init__(self):
        Shape.__init__(self)

    def drawSphere(self, radius = 2, scanAngle = 30):
        alpha = theta = scanAngle
        alphaStep = thetaStep = 0

        while(alphaStep <= 180):
            while(thetaStep <= 360):
                print("a")
                x1, y1, z1 = self.calculateSphericalCoordinates(radius, alphaStep, thetaStep)
            
                thetaStep += theta    
                x2, y2, z2 = self.calculateSphericalCoordinates(radius, alphaStep, thetaStep)
            
                alphaStep += alpha
                x3, y3, z3 = self.calculateSphericalCoordinates(radius, alphaStep, thetaStep)

                x4, y4, z4 = self.calculateSphericalCoordinates(radius, alphaStep, thetaStep - theta)
                
                alphaStep -= alpha

                self.addVertice(x1, y1, z1)
                self.addVertice(x2, y2, z2)
                self.addVertice(x3, y3, z3)
                self.addVertice(x4, y4, z4)
            thetaStep = 0
            alphaStep += alpha

    def calculateRadian(self, degree):
        return degree * (math.pi / 180)   
    
    def calculateSphericalCoordinates(self, r, alpha, theta):
        alpha_radian = self.calculateRadian(alpha)
        theta_radian = self.calculateRadian(theta)

        x = r * math.sin(alpha_radian) * math.cos(theta_radian)
        y = r * math.sin(alpha_radian) * math.sin(theta_radian)
        z = r * math.cos(alpha_radian)
        return x, y, z
    
    def addVerticesOfShape(self, shape):
        for i in shape.getShape():
            self.addVertice(i.getX(), i.getY(), i.getZ())

    def __str__(self):
        return Shape.__str__(self)


if __name__ == "__main__":
    a = Sphere()