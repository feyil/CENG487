from Vec3d import Vec3d
import copy

class ColorRGBA(Vec3d):

    def __init__(self, r, g, b, a):
        Vec3d.__init__(self, r, g, b, a)

    def getR(self):
        return self.getX()

    def getG(self):
        return self.getY()

    def getB(self):
        return self.getZ()

    def getA(self):
        return self.getW()
    