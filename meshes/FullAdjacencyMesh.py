
from Mesh import Mesh


class FullAdjacenyMesh(Mesh):

    def __init__(self, verticeList, faceList):
        Mesh.__init__(self, verticeList, faceList)

        # Edge Adjacency Table
        # e0: v0, v1; F0,-; -,e2,e1,-
        edgeAT = []

        # Face Adjacency Table
        # F0: v0,v1,v2; F1,-,-; e0,e2,e0
        faceAT = []

        # Vertex Adjacency Table
        # v0: v1,v2; F0; e0,e2
        vertexAT = []

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

if __name__ == "__main__":
    a = FullAdjacenyMesh([], [])