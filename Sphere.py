from Primitives3D import Primitive3D

class Sphere(Primitive3D):

    def __init__(self):
        Primitive3D.__init__(self)

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

    def __str__(self):
        return Primitive3D.__str__(self)


if __name__ == "__main__":
    a = Sphere()