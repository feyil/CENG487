# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

import sys

from drawers import *
from parsers import *
from windows import *
from cameras import *
from shapes import *
from scenes import *
from subdividers import *

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
shape.setSubdivider(SubdividerType.CATMULL_CLARK_SUBDIVIDER)


mainScene.addShape("mainShape", shape)
# --------------- end --------------------


# ----------- Choose active camera for the view ----------
mainScene.selectCamera("mainCamera")
# --------------- end ---------------------

def main():
	#mainWindow = InteractiveWindow("App", 800, 600)
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

