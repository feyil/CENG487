# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from enum import Enum
from Box import Box
from Sphere import Sphere
from Mat3d import Mat3d
from Vec3d import Vec3d
from Camera import Camera
from Shape import Shape

class Space(Enum):
    LOCAL = 0
    SCENE = 1

class Scene:

    def __init__(self, sceneName):
        self.__sceneName = sceneName

        self.__cameraList = {}
        self.__activeCam = 0

        self.__shapeListLS = {}    # shapes in their local space
        self.__shapeListSS = {}    # shapes in their scene space
        
    def addShape(self, shapeName, shape):
        self.__shapeListLS.update({shapeName : shape.clone()})

        self.updateShapeListSS(shapeName)
        
    def updateShapeListSS(self, shapeName):
        # When local space object changes update scene space
        shapeLS = self.__shapeListLS.get(shapeName)
        
        newShapeSS = shapeLS.clone()
       
        if shapeName in self.__shapeListSS:
            shapeSS = self.__shapeListSS.get(shapeName)
            shapeSS_FTM = shapeSS.getFinalTransformationMatrix()
            
            newShapeSS.setFinalTransformationMatrix(shapeSS_FTM)
            newShapeSS.transformShape()
        else:
            newShapeSS.setFinalTransformationMatrix(self.__identityMatrix())
        
        self.__shapeListSS.update({shapeName : newShapeSS})

    def __identityMatrix(self):
        return Mat3d().defineMatrix(Vec3d(1,0,0,0),
                                    Vec3d(0,1,0,0),
                                    Vec3d(0,0,1,0),
                                    Vec3d(0,0,0,1))

    def linearMoveShapeto(self, shapeName, x, y, z, tranformationSpace = Space.SCENE):
        if(tranformationSpace == Space.SCENE):
            # Scene Space
            shape = self.__shapeListSS.get(shapeName)
        
            # Shape class logic not work as I expected
            shape.addTransformation(Mat3d().defineTranslationMatrix(x,y,z))
            shape.transformShape(Mat3d().defineTranslationMatrix(x,y,z))
        else:
            # Local Space
            shape = self.__shapeListLS.get(shapeName)
            
            shape.addTransformation(Mat3d().defineTranslationMatrix(x, y, z))
            shape.transformShape(Mat3d().defineTranslationMatrix(x, y, z))

            self.updateShapeListSS(shapeName) # Update Scene Space
    
    def rotateMoveShapeTo(self, shapeName, angle, rotAx = "Y", transformationSpace = Space.SCENE):
        if(transformationSpace == Space.SCENE):
            shape = self.__shapeListSS.get(shapeName)

            shape.addTransformation(Mat3d().defineRotationMatrix(angle, rotAx))
            shape.transformShape(Mat3d().defineRotationMatrix(angle, rotAx))
        else:
            shape = self.__shapeListLS.get(shapeName)
            
            shape.addTransformation(Mat3d().defineRotationMatrix(angle, rotAx))
            shape.transformShape(Mat3d().defineRotationMatrix(angle, rotAx))
            
            self.updateShapeListSS(shapeName)
        
    def removeShape(self, shapeName):
        self.__shapeListLS.pop(shapeName)
        self.__shapeListSS.pop(shapeName)

    def addCamera(self, cameraName, camera):
        self.__cameraList.update({cameraName : camera.clone()})
        
    def selectCamera(self, cameraName):
        # return selected camera
        self.__activeCam = self.__cameraList.get(cameraName)
        return  self.__activeCam

    def getActiveCamere(self):
        return self.__activeCam
    def removeCamera(self, cameraName):
        self.__cameraList.pop(cameraName)

    def renderScene(self):
        print("renderScene")

    def drawGL(self):
        for i in self.__shapeListSS.values():
            # It may not be efficent I am thinking on it.
            i = self.__activeCam.view(i)
            i.drawGL()

    def __str__(self):
        return "Scene"


if __name__ == "__main__":
    a = Scene("main")
    a.addShape("box", Box())
    a.addShape("spehere", Sphere())