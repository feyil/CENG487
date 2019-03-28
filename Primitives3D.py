from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Primitive3D(Shape):

    def __init__(self):
        Shape.__init__(self)

    def calculateRadian(self, degree):
        return degree * (math.pi / 180)  

    def calculatePolarCoordinate(self, r, degree):
        radian = self.calculateRadian(degree)
        a = r * math.cos(radian)
        b = r * math.sin(radian)
        return a, b

    def calculateSphericalCoordinates(self, r, alpha, theta):
        alpha_radian = self.calculateRadian(alpha)
        theta_radian = self.calculateRadian(theta)

        x = r * math.sin(alpha_radian) * math.cos(theta_radian)
        y = r * math.sin(alpha_radian) * math.sin(theta_radian)
        z = r * math.cos(alpha_radian)
        return x, y, z

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

    def __str__(self):
        return Shape.__str__(self)
    
