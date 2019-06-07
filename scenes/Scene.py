# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import * # for now

from shapes import Box, Sphere, Shape
from utils import Vec3d, Mat3d
from cameras import Camera
from drawers import Drawer, DrawStyle

from lights import Light

class Space:
    LOCAL = 0
    SCENE = 1

class Scene:

    def __init__(self, sceneName):
        self.__sceneName = sceneName

        self.__cameraList = {}
        self.__activeCam = 0

        self.__shapeListLS = {}    # shapes in their local space
        self.__shapeListSS = {}    # shapes in their scene space

        self.__drawStyle = DrawStyle.SMOOTH

        self.__lights = []
        self.__lightsStatus = False

    def addLight(self, light):
        self.__lights.append(light)

    def lightsON(self, status=True):
        self.__lightsStatus = status

    def lightON(self, lightNum, status):
        for light in self.__lights:
            if(lightNum == light.getLightNum()):
                light.lightON(status)
    
    def getLightsStatus(self):
        return self.__lightsStatus

    def getLightStatus(self, lightNum):
        for light in self.__lights:
            if(lightNum == light.getLightNum()):
                return light.getLightStatus()

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

    def getActiveCamera(self):
        return self.__activeCam

    def removeCamera(self, cameraName):
        self.__cameraList.pop(cameraName)

    def subdivide(self, shapeName, value):
        shape = self.__shapeListLS.get(shapeName)
        shape.subdivide(value)
        self.updateShapeListSS(shapeName)
        
    def setDrawStyle(self, drawStyle):
        self.__drawStyle = drawStyle

    def draw(self):
      
        for i in self.__shapeListSS.values():
            # I will break camera class coupling with the shape class
            # It may not be efficent I am thinking on it.
            i.setDrawStyle(self.__drawStyle)
            i = self.__activeCam.view(i)
            i.draw()

        Light.lightsON(self.__lightsStatus)
        for light in self.__lights:
            if(light.getLightStatus()):
                light = self.__activeCam.view(light)
                light.draw()

    def __str__(self):
        return "Scene"


if __name__ == "__main__":
    a = Scene("main")
    a.addShape("box", Box())
    a.addShape("spehere", Sphere())