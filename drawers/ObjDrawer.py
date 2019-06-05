# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import *

from Drawer import *
from utils import Vec3d


class ObjDrawer(Drawer):

    def __init__(self):
        Drawer.__init__(self)
    
    def draw(self):
        for face in self._faceList:
            if(self._drawStyle == DrawStyle.SMOOTH or self._drawStyle == DrawStyle.WIRE_ON_SHADED):
                self.drawSmooth(face)
            if(self._drawStyle == DrawStyle.WIRE or self._drawStyle == DrawStyle.WIRE_ON_SHADED):
                self.drawWire(face)

    def drawSmooth(self, face):
        color = 0

        glBegin(GL_POLYGON)
        for verticeIndex in face:
            color += 1
            if(self._color != None):
                glColor3f(self._color.getR(), self._color.getG(), self._color.getB())
            elif(color % 2 == 0):
			    glColor3f(0.8, 0.3, 0.8)
            else:
			    glColor3f(0.2, 0.8, 0.3)
            vertice = self._verticeList[verticeIndex]
            glVertex3f(vertice.getX(), vertice.getY(), vertice.getZ())
        glEnd()

    def drawWire(self, face):
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(self._wireWidth)
                
        glBegin(GL_POLYGON)
        # Sets wire color
        glColor3f(self._wireColor.getX(), self._wireColor.getY(), self._wireColor.getZ())

        for verticeIndex in face:
            vertice = self._verticeList[verticeIndex]
            glVertex3f(vertice.getX(), vertice.getY(), vertice.getZ())
            
        glEnd()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)



if __name__ == "__main__":
    obj = ObjDrawer()
