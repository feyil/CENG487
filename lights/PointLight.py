from OpenGL.GL import *

from Light import Light
from utils import Vec3d, Mat3d
from drawers import LegacyDrawer
from shapes import Box
from materials import MaterialDefs, Material

import copy

class PointLight(Light):
    positionDefault = [0.0, 0.0, 1.0, 1.0]
    constantAttenuationDefault = 1
    linearAttenuationDefault = 0.0
    quadraticAttnuationDefault = 0.0

    def __init__(self, lightName, lightNum, 
                    ambient = Light.ambientDefault,
                    diffuse = Light.diffuseDefault, 
                    specular = Light.specularDefault,
                    position = positionDefault,
                    atConstant = constantAttenuationDefault,
                    atLinear = linearAttenuationDefault,
                    atQuadratic = quadraticAttnuationDefault):

        Light.__init__(self, lightName, lightNum, ambient, diffuse, specular)

        self.__position = Vec3d(position[0], position[1], position[2], 1)

        self.__atConstant = atConstant
        self.__atLinear = atLinear
        self.__atQuadratic = atQuadratic
        
        

    def transformShape(self, aMath3d):
        # Tricky implementation for now 
        # It places light shape to where the light is located in that moment    
        self.placeRepresentativeShape(aMath3d)

        self.__position = aMath3d.multiplyByVec3d(self.__position)
        
        return self

    def clone(self):
        return copy.deepcopy(self)

    def placeRepresentativeShape(self, aMath3d):
        lightBox = self.createRepresentativeShape()

        t = self.__position
        lightBox.addTransformation(Mat3d().defineTranslationMatrix(t.getX(),t.getY(),t.getZ()))
        lightBox.transformShape(Mat3d().defineTranslationMatrix(t.getX(),t.getY(),t.getZ()))

        lightBox.transformShape(aMath3d)
        lightBox.draw()

    def createRepresentativeShape(self):
        drawer = LegacyDrawer()
        lightBox = Box()
        lightBox.setDrawer(drawer)
        lightBox.create()

        # material can be defined to match with light color
        lightBox.setMaterial(Material(**MaterialDefs.LIGHT_BOX))
        
        return lightBox

    def draw(self):
         #status = self._lightStatus
        light = self._lightNum

        # if(status):
        #     glDisable(self._lightNum)
        #     self._lightStatus = False
        
        glLightfv(light, GL_AMBIENT, self._ambient.getVec3d())
        glLightfv(light, GL_DIFFUSE, self._diffuse.getVec3d())
        glLightfv(light, GL_SPECULAR, self._specular.getVec3d())
        glLightfv(light, GL_POSITION, self.__position.getVec3d())

        glEnable(self._lightNum)