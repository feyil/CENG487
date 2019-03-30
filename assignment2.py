# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *

from Window import WindowGL


from Shape import Shape
from Sphere import Sphere
from Cylinder import Cylinder
from Box import Box

from Mat3d import Mat3d

import math

box = Box()
box.drawAs(GL_QUADS)

box.addTransformation(Mat3d().defineRotationMatrix(30, "Z"))
box.addTransformation(Mat3d().defineTranslationMatrix(0, 1, 0))

box.draw()
box.transformShape()

def main():
	mainWindow = WindowGL("App", 800, 600)
	mainWindow.setScene(box)
	mainWindow.run()
	
main()

