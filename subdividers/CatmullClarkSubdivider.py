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

        #TODO introduce faceList

    def addVertex(self, vertex):
        # it is not efficent probably 
        index = len(self.__vertexList)
        self.__vertexList.append(vertex)

        return index

    def getVertex(self, vertexNum):
        return self.__vertexList[vertexNum]

    def getMesh(self):
        return self.__mesh

    def subdivide(self, indicator="+"):
        print("Catmull Abi")
        index = self.calculateEdgePoint(12)
        print(self.getVertex(index))
        pass

    def subdivideFace(self, faceNum):
        pass

    def calculateFacePoint(self, faceNum):
        if(faceNum in self.__facePointDict):
            return self.__facePointDict[faceNum]

        mesh = self.getMesh()
        averageList = []

        vertices = mesh.faceToVertices(faceNum)
        for vertexNum in vertices:
            vertex = mesh.getVertex(vertexNum)
            averageList.append(vertex)

        facePoint = self.calculateAverageOfVertices(averageList)
        
        index = self.addVertex(facePoint)
        self.__facePointDict[faceNum] = index
        
        return index

    def calculateEdgePoint(self, edgeNum):
        if(edgeNum in self.__edgePointDict):
            return self.__edgePointDict[edgeNum]

        mesh = self.getMesh()
        averageList = []

        vertexNums = mesh.edgeToVertices(edgeNum)
        for vertexNum in vertexNums:
            vertex = mesh.getVertex(vertexNum)
            averageList.append(vertex)

        faceNums = mesh.edgeToFaces(edgeNum)
        for faceNum in faceNums:
            vertexNum = self.calculateFacePoint(faceNum)
            averageList.append(self.getVertex(vertexNum))

        edgePoint = self.calculateAverageOfVertices(averageList)

        index = self.addVertex(edgePoint)
        self.__edgePointDict[edgeNum] = index

        return index

    def calculateVertexPoint(self, vertexNum):
        pass

    def findValenceOfVertex(self, vertexNum):
        pass
    
    def calculateQ(self, vertexNum):
        pass

    def calculateR(self, vertexNum):
        pass

    def calculateAverageOfVertices(self, vertexList):
        counter = 0
        average = Vec3d(0, 0, 0, 0)
        for vertex in vertexList:
            average.addVec3d(vertex)
            counter += 1

        return average.divideBy(counter)

    