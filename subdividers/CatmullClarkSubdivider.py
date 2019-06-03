from Subdivider import Subdivider
from meshes import *

class CatmullClarkSubdivider(Subdivider):

    def __init__(self, shape):
        Subdivider.__init__(self, shape)

        self.__mesh = FullAdjacenyMesh(self.getShape().getVerticeList(), self.getShape().getFaceList()) 

    def subdivide(self, indicator="+"):
        print("Catmull Abi")
        pass