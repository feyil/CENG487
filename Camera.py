# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

import math
from enum import Enum


from Mat3d import Mat3d
from Vec3d import Vec3d
from Shape import Shape

# Inspired from learnopengl.com

class CamMovement(Enum):
    FORWARD = 0
    BACKWARD = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5

class Camera:

    def __init__(self):
        # Vectors
        self.__cameraPosition = []
        self.__cameraFront = []
        self.__worldUp = []
        
        self.__cameraUp = self.__worldUp
        self.__cameraRight = []
        self.__cameraTarget = []
        self.__cameraDirection = []
        # End

        # Euler Angles
        self.__yaw = 0
        self.__pitch = 0
        # End

        # LookAtMatrix
        self.__lookAtMatrix = []
        # End

    def setCameraPosition(self, x, y, z):
        self.__cameraPosition = Vec3d(x, y, z, 1)
    
    def setCameraFront(self, x, y, z):
        self.__cameraFront = Vec3d(x, y, z, 0)
        
    def setWorldUp(self, x, y, z):
        self.__worldUp = Vec3d(x, y, z, 0)

    def linearMove(self, direction, speed):
        speed = abs(speed)

        if(direction == CamMovement.FORWARD):
            self.__cameraPosition.addVec3d(self.__cameraFront.clone().normalize().scalarMultiplication(speed))
        elif(direction == CamMovement.BACKWARD):
            self.__cameraPosition.substractVec3d(self.__cameraFront.clone().normalize().scalarMultiplication(speed))
        elif(direction == CamMovement.UP):
            self.__cameraPosition.addVec3d(self.__cameraUp.clone().normalize().scalarMultiplication(speed))
        elif(direction == CamMovement.DOWN):
            self.__cameraPosition.substractVec3d(self.__cameraUp.clone().normalize().scalarMultiplication(speed))
        elif(direction == CamMovement.LEFT):
            self.__cameraPosition.substractVec3d(self.__cameraRight.clone().normalize().scalarMultiplication(speed))
        elif(direction == CamMovement.RIGHT):
            self.__cameraPosition.addVec3d(self.__cameraRight.clone().normalize().scalarMultiplication(speed))
        
        self.updateCamera()
    
    def rotateMove(self, xoffset, yoffset, sensitivity = 0.05, constrainPitch = True):

        xoffset *= sensitivity
        yoffset *= sensitivity

        self.__yaw += xoffset
        self.__pitch += yoffset

        if(constrainPitch):
            if(self.__pitch > 89.0):
                self.__pitch = 89.0
            if(self.__pitch < -89.0):
                self.__pitch = -89.0

        self.__updateCameraVectors()

    def updateCamera(self):
        self.__cameraTarget = self.__cameraPosition.clone().addVec3d(self.__cameraFront)
    
        # LookAt matrix first 3 row
        self.__cameraDirection = self.__cameraPosition.clone().substractVec3d(self.__cameraTarget).normalize()
        self.__cameraRight = self.__worldUp.normalize().crossProductVec3d(self.__cameraDirection)
        self.__cameraUp = self.__cameraDirection.crossProductVec3d(self.__cameraRight)
        # End

        # Final lookAt matrix
        self.__lookAtMatrix = self.__defineCameraMatrix(self.__cameraRight, self.__cameraUp, self.__cameraDirection, self.__cameraPosition)
        # End

    def __defineCameraMatrix(self, rightVector, upVector, directionVector, camPosition):
        lookAt = Mat3d()
        translation = Mat3d()
        translation.defineTranslationMatrix(-camPosition.getX(), -camPosition.getY(), -camPosition.getZ())
        lookAt.defineMatrix(rightVector, upVector, directionVector, Vec3d(0,0,0,1.0))
        
        lookAt.multiplyByMat3d(translation)

        return lookAt

    def calculateRadian(self, degree):
        return degree * (math.pi / 180)  
    
    def __updateCameraVectors(self):
        # Calculate front vector
        frontX = math.cos(self.calculateRadian(self.__pitch)) * math.sin(self.calculateRadian(self.__yaw))
        frontY = math.sin(self.calculateRadian(self.__pitch))
        frontZ = math.cos(self.calculateRadian(self.__pitch)) * math.cos(self.calculateRadian(self.__yaw))
        
        self.__cameraFront = Vec3d(-frontX, -frontY, -frontZ, 0).normalize()
        # End
      
        self.updateCamera()

    def view(self, shape):
        shape.transformShape(self.__lookAtMatrix)
    
    def __str__(self):
        return "Hi buddy"


if __name__ == "__main__":
    a = Camera()
