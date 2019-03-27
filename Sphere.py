from Shape import Shape
from Mat3d import Mat3d
from Vec3d import Vec3d

import math

class Sphere(Shape):

    def __init__(self):
        Shape.__init__(self)
        self.defineRectangle(self, 1)

    # Exactly same with Box method I will refactor later
    def calculateScanAngle(self, distance):
        # Distance is how far the quad from center
        # Calculate angle to rotate for a quad to match one edge
        hipotenous = math.sqrt((distance * distance) + 1)
        half_angle_radian = math.acos(distance / hipotenous)
        angle = 2 * (half_angle_radian * 180 / math.pi)
        return angle

    def defineRectangle(self,shape, length):
        # Start from right top and continue counter clockwise
        shape.addVertice(length,length * 1.8,0)
        shape.addVertice(-length,length * 1.8,0)
        shape.addVertice(-length ,-length * 1.8,0)
        shape.addVertice(length,-length * 1.8,0)

    def __str__(self):
        return Shape.__str__(self)
        
    
print("Hello")