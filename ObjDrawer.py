# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019

from OpenGL.GL import *

from Drawer import Drawer
from Vec3d import Vec3d


class ObjDrawer(Drawer):

    def __init__(self):
        Drawer.__init__(self)

    def draw(self):
        glBegin(GL_QUADS)
        color = 0
        for face in self._faceList:
            for verticeIndex in face:
                color += 1
                if(color % 2 == 0):
			        glColor3f(0.8, 0.3, 0.8)
                else:
			        glColor3f(0.2, 0.8, 0.3)
                vertice = self._verticeList[verticeIndex]
                glVertex3f(vertice.getX(), vertice.getY(), vertice.getZ())
        glEnd() 

if __name__ == "__main__":
    obj = ObjDrawer()
