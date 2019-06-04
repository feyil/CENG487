# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from Mesh import Mesh

class FullAdjacenyMesh(object):

    def __init__(self, verticeList, faceList):

        self.__mesh = Mesh(verticeList, faceList) 

        # Edge Adjacency Table
        # e0: v0, v1; F0,-; -,e2,e1,-
        self.__edgeAT = []

        # Face Adjacency Table
        # F0: v0,v1,v2; F1,-,-; e0,e2,e0
        self.__faceAT = []

        # Vertex Adjacency Table
        # v0: v1,v2; F0; e0,e2
        self.__vertexAT = []

        self.initializeMesh()

    def initializeMesh(self):
        print("Mesh Creation Started...")
        self.resetTables()
    
        countEdge = self.numberOfEdges()
        for edgeNum in range(countEdge):
            edgeEntry = self.buildEdgeEntry(edgeNum)
            self.__edgeAT.append(edgeEntry)

        countFace = self.numberOfFaces()
        for faceNum in range(countFace):
            faceEntry = self.buildFaceEntry(faceNum)
            self.__faceAT.append(faceEntry)

        countVertex = self.numberOfVertices()
        for vertexNum in range(countVertex):
            print("------------")
            print(vertexNum)
            vertexEntry = self.buildVertexEntry(vertexNum)
            self.__vertexAT.append(vertexEntry)
        print("Mesh Creation End") 

    def resetTables(self):
        self.__edgeAT = []
        self.__faceAT = []
        self.__vertexAT = []

    def buildEdgeEntry(self, edgeNum):
        base = self.getMesh()
        entry = []
    
        verticeNums = base.edgeToVertices(edgeNum)
        faceNums = base.edgeToFaces(edgeNum)
        edgeNums = base.edgeToEdges(edgeNum)

        entry.append(verticeNums)
        entry.append(faceNums)
        entry.append(edgeNums)

        return entry

    def buildFaceEntry(self, faceNum):
        base = self.getMesh()
        entry = []

        verticeNums = base.faceToVertices(faceNum)
        faceNums = base.faceToFaces(faceNum)
        edgeNums = base.faceToEdges(faceNum)

        entry.append(verticeNums)
        entry.append(faceNums)
        entry.append(edgeNums)

        return entry

    def buildVertexEntry(self, vertexNum):
        base = self.getMesh()
        entry = []

        vertexNums = base.vertexToVertices(vertexNum)
        faceNums = base.vertexToFaces(vertexNum)
        edgeNums = base.vertexToEdges(vertexNum)

        entry.append(vertexNums)
        entry.append(faceNums)
        entry.append(edgeNums)
        
        return entry

    def getMesh(self):
        return self.__mesh

    # Below is interface we need to support
    
    # face
    def faceToVertices(self, faceNum):
        return self.__faceAT[faceNum][0]

    def faceToFaces(self, faceNum):
        return self.__faceAT[faceNum][1]

    def faceToEdges(self, faceNum):
        return self.__faceAT[faceNum][2]

    
    # vertex
    def vertexToVertices(self, vertexNum):
        return self.__vertexAT[vertexNum][0]

    def vertexToFaces(self, vertexNum):
        return self.__vertexAT[vertexNum][1]

    def vertexToEdges(self, vertexNum):
        return self.__vertexAT[vertexNum][2]


    # edge
    def edgeToVertices(self, edgeNum):
        return self.__edgeAT[edgeNum][0]

    def edgeToFaces(self, edgeNum):
        return self.__edgeAT[edgeNum][1]

    def edgeToEdges(self, edgeNum):
        return self.__edgeAT[edgeNum][2]
        

    # utils
    def updateMesh(self, verticeList, faceList):
        base = self.getMesh()
        
        base.updateMesh(verticeList, faceList)
        self.initializeMesh()

    def getVerticeList(self):
        return self.getMesh().getVerticeList()

    def getFaceList(self):
        return self.getMesh().getFaceList()

    def getVertex(self, vertexNum):
        return self.getMesh().getVertex(vertexNum)

    def getFace(self, faceNum):
        return self.getMesh().getFace(faceNum)

    def getEdge(self, edgeNum):
        return self.getMesh().getEdge(edgeNum)

    def numberOfFaces(self):
        return self.getMesh().numberOfFaces()

    def numberOfEdges(self):
        return self.getMesh().numberOfEdges()

    def numberOfVertices(self):
        return self.getMesh().numberOfVertices()
