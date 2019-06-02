
class Mesh:

    def __init__(self, verticeList, faceList):
        self._verticeList = verticeList
        self._faceList = faceList

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
