# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019


from OpenGL.GL import *

from Drawer import Drawer

# Used for Box, Sphere, and Cylinder
class LegacyDrawer(Drawer):

    def __init__(self):
        Drawer.__init__(self)

    def draw(self):
        glBegin(GL_QUADS)
        color = 0
        for i in self._verticeList:
		    color += 1
		    if(color % 2 == 0):
			    glColor3f(0.8, 0.3, 0.8)
		    else:
			    glColor3f(0.2, 0.8, 0.3)
		    glVertex3f(i.getX(), i.getY(), i.getZ())
        glEnd()