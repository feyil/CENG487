


class Mesh:

    def __init__(self, verticeList, faceList):
        self._verticeList = verticeList
        self._faceList = faceList
        self._edgeList = []

        self.createEdgeList()
      
    def faceToVertices(self, face):
        pass
    
    def vertexToFaces(self, vertex):
        pass
    
    def faceToFaces(self, face):
        pass

    def vertexToVertices(self, vertex):
        pass
    
    def edgeToVertices(self, edge):
        pass
    
    def edgeToFaces(self, edge):
        pass

    def getVerticeList(self):
        return self._verticeList

    def getFaceList(self):
        return self._faceList

    def isEdgeExist(self, edge):
        for e in self._edgeList:
            if(edge[0] == e[0] and edge[1] == e[1]):
                return True
            
            if(edge[0] == e[1] and edge[1] == e[0]):
                return True
            
        return False

    def addEdge(self, edge):
        if(self.isEdgeExist(edge) != True):
            self._edgeList.append(edge)
        
    def createEdgeList(self):
        for face in self._faceList:
            indexer = [-1] + range(len(face))
            for index in indexer:
                edge = []
                try :
                    edge.append(face[index])
                    edge.append(face[index + 1])

                    self.addEdge(edge)
                except IndexError:
                    edge = []
        
