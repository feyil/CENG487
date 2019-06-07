
from OpenGL.GL import *

from utils import Vec3d

class Light(object):
    ambientDefault = [0.0, 0.0, 0.0, 1.0]
    diffuseDefault = [1.0, 1.0, 1.0, 1.0]
    specularDefault = [1.0, 1.0, 1.0, 1.0]
    
    LIGHT_NUM = {
        0: GL_LIGHT0,
        1: GL_LIGHT1,
        2: GL_LIGHT2,
        3: GL_LIGHT3,
        4: GL_LIGHT4,
        5: GL_LIGHT5,
        6: GL_LIGHT6,
        7: GL_LIGHT7
    }

    def __init__(self, lightName, lightNum, 
                    ambient = ambientDefault,
                    diffuse = diffuseDefault, 
                    specular = specularDefault):
        
        self._name = lightName
        self._lightNum = Light.LIGHT_NUM[(lightNum % 8)]
        self._lightStatus = True

        self._ambient = Vec3d(*ambient)
        self._diffuse = Vec3d(*diffuse)
        self._specular = Vec3d(*specular)

    def getLightName(self):
        return self._name
    
    def getLightNum(self):
        return self._lightNum

    def getLightAmbient(self):
        return self._ambient

    def getLightDiffuse(self):
        return self._diffuse
    
    def getLightSpecular(self):
        return self._specular
    
    def lightON(self, status=True):
        self._lightStatus = status
    
    def getlightStatus(self):
        return self._lightStatus

    def enableLight(self):
        if(self._lightStatus):
            glEnable(self._lightNum)

    @staticmethod
    def lightsON(logic=True):
        if(logic == True):
            glEnable(GL_LIGHTING)
        else:
            glDisable(GL_LIGHTING)

    # implement them in subclasses
    def transformShape(self, aMath3d):
        # for camera usage
        pass

    def draw(self):
        # for scene usage
        # define glLight stuff here
        pass

  
