
from Mesh import Mesh


class FullAdjacenyMesh(Mesh):

    def __init__(self, verticeList, faceList):
        Mesh.__init__(self, verticeList, faceList)

        # Edge Adjacency Table
        # e0: v0, v1; F0,-; -,e2,e1,-
        self.__edgeAT = []

        # Face Adjacency Table
        # F0: v0,v1,v2; F1,-,-; e0,e2,e0
        self.__faceAT = []

        # Vertex Adjacency Table
        # v0: v1,v2; F0; e0,e2
        self.__vertexAT = []

if __name__ == "__main__":
    a = FullAdjacenyMesh([], [])