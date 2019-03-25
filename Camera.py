
from Mat3d import Mat3d
from Vec3d import Vec3d
from Shape import Shape

class Camera:

    def __init__(self):
        self.__lookAtMatrix = []
        self.__cameraPosition = []
        self.__worldUpVector = []
        self.__targetPosition = []
    
    def reset(self):
        self.__lookAtMatrix = []
        self.__cameraPosition = []
        self.__worldUpVector = []
        self.__targetPosition = []

    def setCameraPosition(self, x, y, z):
        self.__cameraPosition = Vec3d(x,y,z,1)
        return self        

    def setWorldUpVector(self, x, y, z):
        self.__worldUpVector = Vec3d(x, y, z, 0)
        return self

    def setTargetPosition(self, x, y, z):
        self.__targetPosition = Vec3d(x, y, z, 1)
    
    def loadCamera(self):
        # I assume everything ok until at this point
        # Reverse of the actual direction where the camera look at.
        cameraDirectionVector = self.__cameraPosition.clone().substractVec3d(self.__targetPosition)
        rightAxis = self.__worldUpVector.crossProductVec3d(cameraDirectionVector)
        cameraUp = cameraDirectionVector.crossProductVec3d(rightAxis)
      
        translation = Mat3d().defineTranslationMatrix(  -self.__cameraPosition.getX(), 
                                                        -self.__cameraPosition.getY(), 
                                                        -self.__cameraPosition.getZ())
    
        self.__lookAtMatrix = Mat3d()
        self.__lookAtMatrix.defineMatrix(rightAxis, cameraUp, cameraDirectionVector, Vec3d(0,0,0,1)).multiplyByMat3d(translation)
        print(self.__lookAtMatrix)

    def lookAt(self, shape):
        a = shape.clone()
        a.transformShape(self.__lookAtMatrix) 
        return a

    def __str__(self):
        return "Hi buddy"


if __name__ == "__main__":
    print("Hello from Space Universe whatsoever")