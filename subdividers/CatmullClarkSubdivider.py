# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from Subdivider import Subdivider
from meshes import *
from utils import Vec3d
import copy

class CatmullClarkSubdivider(Subdivider):

    def __init__(self, shape):
        Subdivider.__init__(self, shape)

        self.__mesh = Mesh(self.getShape().getVerticeList(), self.getShape().getFaceList()) 

        # Store vertices as Vec3d objects
        self.__vertexList = []
        self.__faceList = []

        # All points to the vertexList indexes
        self.__facePointDict = {}
        self.__edgePointDict = {}
        self.__vertexPointDict = {}

        self.__subdivisionHistory = []

    def addVertex(self, vertex):
        # it is not efficent probably 
        index = len(self.__vertexList)
        self.__vertexList.append(vertex)

        return index

    def getVertex(self, vertexNum):
        return self.__vertexList[vertexNum].clone()

    def getMesh(self):
        return self.__mesh

    def update(self):
        self.__vertexList = []
        self.__faceList = []

        self.__facePointDict = {}
        self.__edgePointDict = {}
        self.__vertexPointDict = {}

    def updateShape(self, vertexList, faceList):
        mesh = self.getMesh()
        shape = self.getShape()
        
        mesh.updateMesh(vertexList, faceList)

        shape.setVerticeList(vertexList)
        shape.setFaceList(faceList)
        shape.setSize(len(vertexList))
    
    def addToHistory(self):
        shape = self.getShape()

        self.__subdivisionHistory.append(shape.getFaceList())
        self.__subdivisionHistory.append(shape.getVerticeList())

    def backToHistory(self):
        if(len(self.__subdivisionHistory) != 0):
            self.updateShape(self.__subdivisionHistory.pop(), self.__subdivisionHistory.pop())

    def subdivide(self, indicator="+"):
        mesh = self.getMesh()
        
        if(indicator == '+'):
            print("Catmull-Clark subdivision input taken")
            print("Subidivison in progess... wait")
            self.addToHistory()

            faceCount = mesh.numberOfFaces()
            for faceNum in range(faceCount):
                if(faceNum % 10 == 0):
                    print("Progress {0} / {1}".format(faceCount, faceNum))
                dividedFaces = self.subdivideFace(faceNum)
                self.__faceList += dividedFaces
       
            self.updateShape(self.__vertexList, self.__faceList)
            print("Subidivison Done")
        elif(indicator == '-'):
            self.backToHistory()

        # prepare subdivider to the next step
        self.update()
        
    def subdivideFace(self, faceNum):
        mesh = self.getMesh()
   
        # all has references to self.__vertexList
        facePoint = self.calculateFacePoint(faceNum)
        edgePoints = []
        vertexPoints = []

        edgeNums = mesh.faceToEdges(faceNum)
        for edgeNum in edgeNums:
            edgePoint = self.calculateEdgePoint(edgeNum)
            edgePoints.append(edgePoint)

        vertexNums = mesh.faceToVertices(faceNum)
        for vertexNum in vertexNums:
            vertexPoint = self.calculateVertexPoint(vertexNum)
            vertexPoints.append(vertexPoint)

        dividedFaces = self.connectDivisionQuad(facePoint, edgePoints, vertexPoints)

        return dividedFaces
     
    def connectDivisionQuad(self, facePoint, edgePoints, vertexPoints):
        dividedFaces = []

        # I found it by try and error
        f0 = [vertexPoints[3], edgePoints[0], facePoint, edgePoints[3]]
        f1 = [vertexPoints[0], edgePoints[1], facePoint, edgePoints[0]]
        f2 = [vertexPoints[2], edgePoints[3], facePoint, edgePoints[2]]
        f3 = [vertexPoints[1], edgePoints[2], facePoint, edgePoints[1]]
    
        dividedFaces.append(f0)
        dividedFaces.append(f1)
        dividedFaces.append(f2)
        dividedFaces.append(f3)

        return dividedFaces

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
        if(vertexNum in self.__vertexPointDict):
            return self.__vertexPointDict[vertexNum]

        mesh = self.getMesh()
        vertexPoint = Vec3d(0,0,0,0)

        valence = self.findValenceOfVertex(vertexNum)
        valueQ = self.calculateQ(vertexNum)
        valueR = self.calculateR(vertexNum)
        valueS = mesh.getVertex(vertexNum)

        # (Q + 2R + S(n - 3)) / n
        vertexPoint.addVec3d(valueQ).addVec3d(valueR.scalarMultiplication(2.0)).addVec3d(valueS.scalarMultiplication((valence - 3))).divideBy(float(valence))

        index = self.addVertex(vertexPoint)
        self.__vertexPointDict[vertexNum] = index

        return index
        
    def findValenceOfVertex(self, vertexNum):
        mesh = self.getMesh()
        edgeNums = mesh.vertexToEdges(vertexNum)

        return len(edgeNums)
    
    def calculateQ(self, vertexNum):
        mesh = self.getMesh()
        averageList = []

        faceNums = mesh.vertexToFaces(vertexNum)
        for faceNum in faceNums:
            facePointNum = self.calculateFacePoint(faceNum)
            averageList.append(self.getVertex(facePointNum))

        valueQ = self.calculateAverageOfVertices(averageList)

        return valueQ

    def calculateR(self, vertexNum):
        mesh = self.getMesh()
        averageList = []

        edgeNums = mesh.vertexToEdges(vertexNum)
        for edgeNum in edgeNums:
            midpoint = self.calculateEdgeMidpoint(edgeNum)
            averageList.append(midpoint)

        valueR = self.calculateAverageOfVertices(averageList)

        return valueR

    def calculateEdgeMidpoint(self, edgeNum):
        mesh = self.getMesh()
        averageList = []

        vertexNums = mesh.getEdge(edgeNum)
        for vertexNum in vertexNums:
            vertex = mesh.getVertex(vertexNum)
            averageList.append(vertex)
     
        midpoint = self.calculateAverageOfVertices(averageList)

        return midpoint

    def calculateAverageOfVertices(self, vertexList):
        counter = 0
        average = Vec3d(0, 0, 0, 0)
        for vertex in vertexList:
            average.addVec3d(vertex)
            counter += 1

        return average.divideBy(counter)

    