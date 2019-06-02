# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

import sys

from LegacyDrawer import LegacyDrawer
from ObjDrawer import ObjDrawer
from Drawer import *
from ObjParser import ObjParser

from Window import WindowGL
from InteractiveWindow import InteractiveWindow
from MouseControlledWindow import MouseControlledWindow
from Camera import *

from Sphere import Sphere
from Cylinder import Cylinder
from Box import Box
from Scene import *

# input checking
if(len(sys.argv) != 2):
	print("\nPlease provide .obj file:\n  >python assignment4.py *.obj\n")
	exit()

# Create a Scene which has two camera one of them active view
# also has three shape in it.
mainScene = Scene("mainScene")

# ------ mainCamera --------

camera = Camera()
camera.setCameraFront(0,0,-1)
camera.setCameraPosition(0,0,12)
camera.setWorldUp(0,1,0)
camera.updateCamera()

# add to the scene
mainScene.addCamera("mainCamera", camera)

# ------- end --------------

# # ---------- cam2 ----------
# camera2 = Camera()
# camera2.setCameraFront(0,0,1)
# camera2.setCameraPosition(0,0,-12)
# camera2.setWorldUp(0,1,0)
# camera2.updateCamera()

# # add to the scene
# mainScene.addCamera("cam2", camera2)

# ----------- end -----------

#----------------- Obj File ------------------
objDrawer = ObjDrawer()

objParser = ObjParser(sys.argv[1])
shape = objParser.parse()

shape.setDrawer(objDrawer)
shape.setDrawStyle(DrawStyle.SMOOTH)


mainScene.addShape("mainShape", shape)
# --------------- end --------------------


# ----------- Choose active camera for the view ----------
mainScene.selectCamera("mainCamera")
# --------------- end ---------------------

def main():
	mainWindow = MouseControlledWindow("App", 800, 600)
	# ---------- set mainScene as the window display source
	mainWindow.setScene(mainScene)
	# --------------- end --------------------------

	# ----------- make some arrangement to fit the screen ------
	# mainWindow.getScene().linearMoveShapeto("box", -4, 0, 0, tranformationSpace=Space.SCENE) # in scene space
	# mainWindow.getScene().linearMoveShapeto("cylinder", 4, 0, 0) # in scene space
	# -------------------- end ----------------------

	# ----------- start the window --------------
	
	mainWindow.run()
	# ---------------- end ----------------------


main()

