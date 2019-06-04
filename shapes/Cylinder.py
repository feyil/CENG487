# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from Primitives3D import Primitive3D

class Cylinder(Primitive3D):

    def __init__(self):
        Primitive3D.__init__(self)
    
    def create(self, r = 1, length = 3, scanAngle = 30):
        step = scanAngle
        
        self.subdivison = {"angle" : scanAngle}
        
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

    def __str__(self):
        return Primitive3D.__str__(self)
        
    
