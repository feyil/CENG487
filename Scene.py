# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from enum import Enum

class Space(Enum):
    LOCAL = 0
    SCENE = 1

class Scene:

    def __init__(self, sceneName):
        print("Scene")
        self.__sceneName = sceneName

        self.cameraList = []

        self.__objectListLS = []    # Objects in their local space
        self.__objectListSS = []    # Objects in their scene space
        
        self.__objectListCamsView = [] # Objects camera viewed

    def addObject(self, objectName, object):
        print("addObject")

    def moveObjectTo(self, x, y, z):
        print("moveObject")

    def removeObject(self, objectName):
        print("removeObject")

    def addTransformationToObject(self, objectName, tranformation, tranformationSpace = Space.SCENE):
        print("addTransformationtoSceneSpaceObject")

    def transformObject(self, objectName, transformation = 0, transformationSpace = Space.SCENE):
        print("transformObject")

    def addCamera(self, cameraName, camera):
        print("addCamera")

    def selectCamera(self, cameraName):
        print("selectCamera")
        # return selected camera

    def removeCamera(self, cameraName):
        print("removeCamera")

    def renderScene(self):
        print("renderScene")

    def drawGL(self):
        print("drawGL")

    def __str__(self):
        return "Scene"

            
