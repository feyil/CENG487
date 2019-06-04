
import copy

class Mesh:

    def __init__(self, verticeList, faceList):
        self._verticeList = verticeList
        self._faceList = faceList
        self._edgeList = []

        self.createEdgeList()

    def updateMesh(self, verticeList, faceList):
        self._verticeList = verticeList
        self._faceList = faceList
        self._edgeList = []
        
        self.createEdgeList()
        
    # getters
    def getVertex(self, vertexNum):
        return self._verticeList[vertexNum].clone()
        
    def getFace(self, faceNum):
        return copy.copy(self._faceList[faceNum])

    def getEdge(self, edgeNum):
        return copy.copy(self._edgeList[edgeNum])

    def numberOfFaces(self):
        return len(self._faceList)

    # face  
    def faceToVertices(self, faceNum):
        return self._faceList[faceNum]

    def faceToFaces(self, faceNum):
        faces = set()

        edges = self.faceToEdges(faceNum)
        for edgeNum in edges:
            faceList = self.edgeToFaces(edgeNum)
            for face in faceList:
                faces.add(face) 
        
        faces = list(faces)
        faces.remove(faceNum)

        return faces

    def faceToEdges(self, faceNum):
        edgeNums = []

        face = self._faceList[faceNum]
        edges = self.discoverEdges(face)

        for edge in edges:
            edgeNum = self.findEdgeNum(edge)
            edgeNums.append(edgeNum)
        
        return edgeNums

    
    # vertex
    def vertexToVertices(self, vertexNum):
        vertexNums = set()

        edges = self.vertexToEdges(vertexNum)
        for edge in edges:
            vertices = self.edgeToVertices(edge)
            for vertex in vertices:
                vertexNums.add(vertex)

        vertexNums = list(vertexNums)
        vertexNums.remove(vertexNum)

        return vertexNums
    
    def vertexToFaces(self, vertexNum):
        faceNums = []

        counter = 0
        for face in self._faceList:
            for vertex in face:
                if(vertexNum == vertex):
                    faceNums.append(counter)
            counter += 1
        return faceNums

    def vertexToEdges(self, vertexNum):
        edgeNums = []

        counter = 0
        for edge in self._edgeList:
            if(vertexNum in edge):
                edgeNums.append(counter)
            
            counter += 1

        return edgeNums

    # edge
    def edgeToVertices(self, edgeNum):
        return self._edgeList[edgeNum]

    def edgeToFaces(self, edgeNum):
        faces = []

        maxFaceNum = len(self._faceList)

        for faceNum in range(maxFaceNum):
            edges = self.faceToEdges(faceNum)
            if(edgeNum in edges):
                faces.append(faceNum)
                  
        return faces
                
    def edgeToEdges(self, edgeNum):
        edgeNums = set()

        vertices = self.edgeToVertices(edgeNum)
        for vertex in vertices:
            edges = self.vertexToEdges(vertex)
            for edge in edges:
                edgeNums.add(edge)
        
        edgeNums = list(edgeNums)
        edgeNums.remove(edgeNum)

        return edgeNums
        

    # utils
    def getVerticeList(self):
        return self._verticeList

    def getFaceList(self):
        return self._faceList
    
    def createEdgeList(self):
        for face in self._faceList:
            edges = self.discoverEdges(face)
            for edge in edges:
                self.addEdge(edge)
        
    def discoverEdges(self, face):
        edges = []

        indexer = [-1] + range(len(face))
        for index in indexer:
            edge = []
            try:
                edge.append(face[index])
                edge.append(face[index + 1])

                edges.append(edge)
            except IndexError:
                edge = []
        
        return edges

    def addEdge(self, edge):
        if(self.isEdgeExist(edge) != True):
            self._edgeList.append(edge)

    def isEdgeExist(self, edge):
        if(self.findEdgeNum(edge) != None):
            return True
    
        return False

    def findEdgeNum(self, edge):
        counter = 0
        for e in self._edgeList:
            if(edge[0] == e[0] and edge[1] == e[1]):
                return counter
            
            if(edge[0] == e[1] and edge[1] == e[0]):
                return counter
            
            counter += 1
        
        return None
