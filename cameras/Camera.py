# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

import math
import copy

from utils import Vec3d, Mat3d
from shapes import Shape

# Inspired from learnopengl.com

# Used for enumeration purposes
class CamMovement:
    FORWARD = 0
    BACKWARD = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5

class CamFocus:
    FREE_MOVE = 0
    FOCUS_TARGET = 1

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

        # CamFocus
        self.__camFocus = CamFocus.FREE_MOVE

        # Target to Focus
        self.__target = None
        self.__rotated = 0

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

        self.setTarget(self.__cameraTarget.getX(), self.__cameraTarget.getY(), self.__cameraDirection.getZ())
    
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

    def rotateCamera(self, degree, axis="X"):
        self.__rotated += degree
        radian = self.calculateRadian(self.__rotated)

        self.setFocus(CamFocus.FOCUS_TARGET)
        if(self.__target == None):
            self.setTarget(0,0,0)
        

        if(axis == "X"):
            # derivative
            self.setWorldUp(0, math.cos(radian), math.sin(radian))
        if(axis == "Y"):
            self.setWorldUp(0, 1, 0)
        rotMat = Mat3d().defineRotationMatrix(degree, axis)
    
        self.__cameraPosition = rotMat.multiplyByVec3d(self.__cameraPosition)
    
        self.__updateCameraVectors()

        self.setFocus(CamFocus.FREE_MOVE)
       
    def __calculateTarget(self):
        if(self.__camFocus == CamFocus.FREE_MOVE):
            self.__cameraTarget = self.__cameraPosition.clone().addVec3d(self.__cameraFront)
        elif(self.__camFocus == CamFocus.FOCUS_TARGET):
            self.__cameraTarget = self.__target

    def setTarget(self, targetX, targetY, targetZ):
        self.__target = Vec3d(targetX, targetY, targetZ, 0)

    def setFocus(self, camFocus = CamFocus.FREE_MOVE):
        self.__camFocus = camFocus

    def updateCamera(self):
        self.__calculateTarget()
    
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
        return float(degree) * (math.pi / 180)  
    
    def __updateCameraVectors(self):
        # Calculate front vector
        frontX = math.cos(self.calculateRadian(self.__pitch)) * math.sin(self.calculateRadian(self.__yaw))
        frontY = math.sin(self.calculateRadian(self.__pitch))
        frontZ = math.cos(self.calculateRadian(self.__pitch)) * math.cos(self.calculateRadian(self.__yaw))
        
        self.__cameraFront = Vec3d(-frontX, -frontY, -frontZ, 0).normalize()
        # End
      
        self.updateCamera()

    def view(self, shape):
        return shape.clone().transformShape(self.__lookAtMatrix)
    
    def __str__(self):
        output = ""
        output += "Camera Position:\n {0}\n".format(self.__cameraPosition)
        output += "Camera Target:\n {0}\n".format(self.__cameraTarget)
        output += "Camera Front:\n {0}\n".format(self.__cameraFront)
        output += "Yaw Angle: {0}\n".format(self.__yaw)
        output += "Pitch Angle: {0}\n".format(self.__pitch)
        return output

    def clone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    a = Camera()
