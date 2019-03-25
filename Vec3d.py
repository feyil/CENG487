# CENG 487 Assignment1 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

import math # for sqrt
import copy # for clone impl

class Vec3d:
    # length can be stored here to quick access
  
    def __init__(self, x, y, z, w):
        self.__vector = [x, y, z, w]
        
    def dotProductVec3d(self, aVec3d):
        if(self.__vector[-1] == 0):
            vect = aVec3d.getVec3d()
            result = 0
            for i in range(3):
                result += self.__vector[i] * vect[i]
            return result
            
    def crossProductVec3d(self, aVec3d): 
        # dot check wheter vector or point
        x, y, z, _ = self.__vector
        a, b, c, _ = aVec3d.getVec3d()
        return Vec3d((y * c) - (b * z), (a * z) - (x * c), (x * b) - (a * y), 0)
            
    def projectionOntoVec3d(self, aBasisVec3d):
        if(self.__vector[-1] == 0):
            value = self.dotProductVec3d(aBasisVec3d) / float(aBasisVec3d.lengthSquare())
            return aBasisVec3d.clone().scalarMultiplication(value)

    def calculateAngleVec3d(self, aVec3d):
        if(self.__vector[-1] == 0):
            cosx = self.dotProductVec3d(aVec3d) / (float(self.length()) * aVec3d.length())
            degrees = (math.acos(cosx) * 180.0) / math.pi
            return degrees
        
    def addVec3d(self, aVect3d):
        vect = aVect3d.getVec3d()
        for i in range(4):
            self.__vector[i] += vect[i]
        return self
    
    def substractVec3d(self, aVect3d):
        vect = aVect3d.getVec3d()
        for i in range(4):
            self.__vector[i] -= vect[i]
        return self
    
    def scalarMultiplication(self, value):
        for i in range(4):
            self.__vector[i] *= value
        return self
        
    # length calculation in homegenous coordinate or ??
    def length(self):
        return math.sqrt(self.lengthSquare())

    def lengthSquare(self):
        sum = 0
        for i in range(3):
            sum += self.__vector[i] ** 2
        return sum
    
    def normalize(self):
        if(self.length() == 0):
            self.scalarMultiplication(0)
        else:
            self.scalarMultiplication(1 / self.length())
        return self

    def getX(self):
        return self.__vector[0]

    def getY(self):
        return self.__vector[1]
    
    def getZ(self):
        return self.__vector[2]
    
    def getVec3d(self):
        return self.__vector

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return "Vec3d: \n\t" + self.__vector.__str__()
    

        
if __name__ == "__main__":
    a = Vec3d(1,2,3,0)
    a.crossProductVec3d(Vec3d(1,2,5,0))
    print(a)