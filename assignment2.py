# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *

from Window import WindowGL
from Camera import *


from Shape import Shape
from Sphere import Sphere
from Cylinder import Cylinder
from Box import Box

from Mat3d import Mat3d

import math



# --------------------- TESTED --------------------- #
# box = Box()
# box.drawAs(GL_QUADS)
# box.draw()
# camera = Camera()
# camera.setCameraFront(0,0,-1)
# camera.setCameraPosition(0,0,6)
# camera.setWorldUp(0,1,0)
# camera.updateCamera()

# camera.linearMove(CamMovement.BACKWARD, 4)
# camera.linearMove(CamMovement.RIGHT, 2)

# camera.rotateMove(5,10, sensitivity = 1)
# camera.linearMove(CamMovement.RIGHT, 1)
# camera.view(box)
# --------------------- TESTED  END--------------------- #

box = Sphere()
box.drawAs(GL_QUADS)
box.draw()
camera = Camera()
camera.setCameraFront(0,0,-1)
camera.setCameraPosition(0,0,6)
camera.setWorldUp(0,1,0)
camera.updateCamera()
camera.view(box)
print(camera)

def main():
	mainWindow = WindowGL("App", 800, 600)
	mainWindow.setScene(box)
	mainWindow.run()
	
main()

