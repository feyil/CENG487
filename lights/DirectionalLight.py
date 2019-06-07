# CENG 487 Assignment5 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import *

from Light import Light
from utils import Vec3d, Mat3d

import copy

class DirectionalLight(Light):
    directionDefault = [0.0, 0.0, 1.0, 0.0]

    def __init__(self, lightName, lightNum, 
                    ambient = Light.ambientDefault,
                    diffuse = Light.diffuseDefault, 
                    specular = Light.specularDefault,
                    direction = directionDefault):
        
        Light.__init__(self, lightName, lightNum, ambient, diffuse, specular)

        self.__direction = Vec3d(direction[0], direction[1], direction[2], 0.0)

    def transformShape(self, aMath3d):
        self.__direction = aMath3d.multiplyByVec3d(self.__direction)
        return self
    
    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        #status = self._lightStatus
        light = self._lightNum

        # if(status):
        #     glDisable(self._lightNum)
        #     self._lightStatus = False
        
        glLightfv(light, GL_AMBIENT, self._ambient.getVec3d())
        glLightfv(light, GL_DIFFUSE, self._diffuse.getVec3d())
        glLightfv(light, GL_SPECULAR, self._specular.getVec3d())
        glLightfv(light, GL_POSITION, self.__direction.getVec3d())

        self.enableLight()