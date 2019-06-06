from OpenGL.GL import * 

from utils import Vec3d

class Material(object):

    # defining default values    
    ambientDefault = [0.2, 0.2, 0.2, 1.0]
    diffuseDefault = [0.8, 0.8, 0.8, 1.0]
    specularDefault = [0, 0.0, 0.0, 1.0]
    shininessDefault = 0.0
    emmissionDefault = [0.0, 0.0, 0.0, 1.0]

    def __init__(self, materialName, 
                    ambient = ambientDefault, 
                    diffuse = diffuseDefault, 
                    specular = specularDefault, 
                    shininess = shininessDefault, 
                    emission = emmissionDefault):

        self.__materialName = materialName
        self.__ambient = Vec3d(*ambient)
        self.__diffuse = Vec3d(*diffuse)
        self.__specular = Vec3d(*specular)
        self.__shininess = shininess
        self.__emission = Vec3d(*emission)
    
    def applyMaterial(self, face = GL_FRONT_AND_BACK):
        glMaterialfv(face, GL_AMBIENT, self.__ambient.getVec3d())
        glMaterialfv(face, GL_DIFFUSE, self.__diffuse.getVec3d())
        glMaterialfv(face, GL_SPECULAR, self.__specular.getVec3d())
        glMaterialfv(face, GL_SHININESS, self.__shininess)
        glMaterialfv(face, GL_EMISSION, self.__emission.getVec3d())
    
    def getMaterialName(self):
        return self.__materialName
    
    def getMaterialAmbient(self):
        return self.__ambient.clone()

    def getMaterialDiffuse(self):
        return self.__diffuse.clone()

    def getMaterialSpecular(self):
        return self.__specular.clone()

    def getMaterialShininess(self):
        return self.__shininess

    def getMaterialEmision(self):
        return self.__emission.clone()

    def __str__(self):
        output = ""
        output += "Material Name: {0}\n".format(self.__materialName)
        output += "-> Ambient:\n {0}\n".format(self.__ambient)
        output += "-> Diffuse:\n {0}\n".format(self.__diffuse)
        output += "-> Specular:\n {0}\n".format(self.__specular)
        output += "-> Shininess:\n {0}\n".format(self.__shininess)
        output += "-> Emision:\n {0}\n".format(self.__emission)
        
        return output