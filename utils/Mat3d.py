# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

import math
import copy
from Vec3d import Vec3d

class Mat3d:
    # Possible transformation types:
    #   Translation 
    #   Rotation X, Y, Z
    #   Scaling
    #   Custom
    #   None

    def __init__(self):
        self.__matrix = self.__zeroMatrix()
        self.__transformationType = "None"
    
    def __zeroMatrix(self, m = 4, n = 4):
        return [[0 for i in range(m)] for j in range(n)]

    def defineTranslationMatrix(self, tx, ty, tz):
        self.__matrix = self.__zeroMatrix()
        tList = [tx, ty, tz, 1]
        for i in range(4):
            self.__matrix[i][i] = 1
            self.__matrix[i][-1] = tList[i]
        self.__transformationType = "Translation"
        return self

    def defineRotationMatrix(self, theta, rotationAxis):
        self.__zeroMatrix()
        radian = theta * (math.pi / 180)
        cosx = math.cos(radian)
        sinx = math.sin(radian)
        if(rotationAxis == "X"):
            self.__matrix[0][0] = self.__matrix[3][3] = 1
            self.__matrix[1][1] = self.__matrix[2][2] = cosx
            self.__matrix[2][1] = sinx
            self.__matrix[1][2] = -1 * sinx
        elif(rotationAxis == "Y"):
            self.__matrix[1][1] = self.__matrix[3][3] = 1
            self.__matrix[0][0] = self.__matrix[2][2] = cosx
            self.__matrix[0][2] = sinx
            self.__matrix[2][0] = -1 * sinx
        elif(rotationAxis == "Z"):
            self.__matrix[2][2] = self.__matrix[3][3] = 1
            self.__matrix[0][0] = self.__matrix[1][1] = cosx
            self.__matrix[1][0] = sinx
            self.__matrix[0][1] = -1 * sinx
        else:
            return "Invalid Axis"
        self.__transformationType = "Rotation"
        return self

    def defineScalingMatrix(self, sx, sy, sz):
        self.__matrix = self.__zeroMatrix()
        sList = [sx, sy, sz, 1]
        for i in range(4):
            self.__matrix[i][i] = sList[i]
        self.__transformationType = "Scaling"
        return self

    def defineMatrix(self, v0, v1, v2, v3, flag="row"):
        self.__matrix = [   v0.getVec3d(),
                            v1.getVec3d(),
                            v2.getVec3d(),
                            v3.getVec3d()]
        if(flag == "column"):
            self.takeTranspose()
        return self

    def multiplyByVec3d(self, aVec3d):
        vect = aVec3d.getVec3d()
        rsltVec = [0, 0, 0, 0]
        for i in range(4):
            for j in range(4):
                rsltVec[i] += self.__matrix[i][j] * vect[j]
        return Vec3d(rsltVec[0], rsltVec[1], rsltVec[2], rsltVec[3])

    def multiplyByMat3d(self, aMat3d):
        resultMatrix = []
        aMat3d.takeTranspose()
        for i in range(4):
            vect = []
            for j in range(4):
                vect.append(self.__dotProduct(self.__matrix[i], aMat3d.__matrix[j]))
            resultMatrix.append(vect)
        aMat3d.takeTranspose()
        self.__matrix = resultMatrix
        return self

    def __dotProduct(self, aList, bList):
        value = 0
        for i in range(4):
            value += aList[i] * bList[i]
        return value

    def takeTranspose(self):
        resultMatrix = []
        for i in range(4):
            vect = []
            for j in range(4):
                vect.append(self.__matrix[j][i])
            resultMatrix.append(vect)
        self.__matrix = resultMatrix
        return self

    def getTransformationType(self):
        return self.__transformationType

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        output = "  Transformation: %s" % (self.__transformationType) + "\n"
        for i in self.__matrix:
            output += str(i) + "\n"
        return output


if __name__ == "__main__": 
    a = Mat3d()
    a.defineMatrix(Vec3d(0,5,0,0), Vec3d(0,0,0,3),Vec3d(0,0,2,0),Vec3d(1,0,0,0), "column")
    print(a)

