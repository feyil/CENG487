from Subdivider import Subdivider
from meshes import *
from utils import Vec3d

class CatmullClarkSubdivider(Subdivider):

    def __init__(self, shape):
        Subdivider.__init__(self, shape)

        self.__mesh = FullAdjacenyMesh(self.getShape().getVerticeList(), self.getShape().getFaceList()) 

        # Store vertices as Vec3d objects
        self.__vertexList = []

        # All points to the vertexList indexes
        self.__facePointDict = {}
        self.__edgePointDict = {}
        self.__vertexPointDict = {}

    def getMesh(self):
        return self.__mesh

    def subdivide(self, indicator="+"):
        print("Catmull Abi")
        pass

    def subdivideFace(self, faceNum):
        pass

    def calculateFacePoint(self, faceNum):
        pass

    def calculateEdgePoint(self, edgeNum):
        pass
    
    def calculateVertexPoint(self, vertexNum):
        pass

    def findValenceOfVertex(self, vertexNum):
        pass
    
    def calculateQ(self, vertexNum):
        pass

    def calculateR(self, vertexNum):
        pass



    