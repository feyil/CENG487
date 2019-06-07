from OpenGL.GL import *

from Light import Light
from utils import Vec3d, Mat3d
from drawers import LegacyDrawer
from shapes import Box
from materials import MaterialDefs, Material

import copy

# Near identical implementation with PointLight
# I didn't want to use inheritance to be flexible and independent to point light for now

class SpotLight(Light):
    positionDefault = [0.0, 0.0, 1.0, 1.0]
    constantAttenuationDefault = 1
    linearAttenuationDefault = 0.0
    quadraticAttnuationDefault = 0.0

    # spotlight related
    cutoffDefault = 180.0 # angle
    directionDefault = [0.0, 0.0, -1.0, 0]
    exponentDefault = 0.0 # 0 - 128.0

    def __init__(self, lightName, lightNum, 
                    ambient = Light.ambientDefault,
                    diffuse = Light.diffuseDefault, 
                    specular = Light.specularDefault,
                    position = positionDefault,
                    atConstant = constantAttenuationDefault,
                    atLinear = linearAttenuationDefault,
                    atQuadratic = quadraticAttnuationDefault,
                    cutoff = cutoffDefault,
                    direction = directionDefault,
                    exponent = exponentDefault):
        
        Light.__init__(self, lightName, lightNum, ambient, diffuse, specular)

        self.__position = Vec3d(position[0], position[1], position[2], 1)

        self.__atConstant = atConstant
        self.__atLinear = atLinear
        self.__atQuadratic = atQuadratic

        self.__cutoff = cutoff
        self.__direction = Vec3d(direction[0], direction[1], direction[2], 0)
        self.__exponent = exponent

    def transformShape(self, aMath3d):
        # Tricky implementation for now 
        # It places light shape to where the light is located in that moment    
        self.placeRepresentativeShape(aMath3d)

        self.__position = aMath3d.multiplyByVec3d(self.__position)
        self.__direction = aMath3d.multiplyByVec3d(self.__direction)
        
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

        # attenuation related
        glLightf(light, GL_CONSTANT_ATTENUATION, self.__atConstant)
        glLightf(light, GL_LINEAR_ATTENUATION, self.__atLinear)
        glLightf(light, GL_QUADRATIC_ATTENUATION, self.__atQuadratic)
        
        # spotlight related
        glLightfv(light, GL_SPOT_CUTOFF, self.__cutoff)
        glLightfv(light, GL_SPOT_DIRECTION, self.__direction.getVec3d())
        glLightfv(light, GL_SPOT_EXPONENT, self.__exponent)
    
        self.enableLight()

    