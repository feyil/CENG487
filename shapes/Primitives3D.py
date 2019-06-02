
from shapes import Shape
from utils import Vec3d, Mat3d

import math

class Primitive3D(Shape):

    def __init__(self):
        Shape.__init__(self)

        # {"angle" : 10} {"number" : 1} for now
        self.subdivison = {}

    # value either '+' '-'
    def subdivide(self, value):
        self.resetShape()
        
        if("angle" in self.subdivison):
            angle = self.subdivison.get("angle")

            new_angle = 0

            if(value == '+'):
                new_angle = angle / 2.0
            elif(value == '-'):
                new_angle = angle * 2

            self.create(scanAngle = new_angle)

            self.subdivison = {"angle" : new_angle}
        elif("number" in self.subdivison):
            number = self.subdivison.get("number")
            
            new_number = 0
            if(number == 0):
                number = 1

            if(value == '+'):
                new_number = number * 2
            elif(value == '-'):
                new_number = int(number / 2.0)

            if(new_number == 8): # it have hard times if we exceed this number
                new_number = 4
            self.subdivison = {"number" : new_number}
            self.create(division = new_number)

        
    def create(self, scanAngle = 0, division = 0):
        pass

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
    
