# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from LegacyDrawer import LegacyDrawer

from Window import WindowGL
from InteractiveWindow import InteractiveWindow
from Camera import *

from Sphere import Sphere
from Cylinder import Cylinder
from Box import Box
from Scene import *

# Second camera pitch and yaw movement can jump if we rotate using arrow key 360 degree we can use 
# both camera without any problem. I am looking for the cause of the jump for "cam2"


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


# ---------- cam2 ----------
camera2 = Camera()
camera2.setCameraFront(0,0,1)
camera2.setCameraPosition(0,0,-12)
camera2.setWorldUp(0,1,0)
camera2.updateCamera()

# add to the scene
mainScene.addCamera("cam2", camera2)

# ----------- end -----------
drawer = LegacyDrawer()
# -------- Create a box shape and add to the scene -------

box = Box()
box.create(0) # subdivision
box.setDrawer(drawer)
mainScene.addShape("box", box)

# ------------ end -------------------

# ---------- Create a sphere and add to the scene ----------
sphere = Sphere()
sphere.setDrawer(drawer)
sphere.create(scanAngle=30) # subdivision

mainScene.addShape("sphere", sphere)
# ------------ end ----------------

# ---------- Create a cylinder and add to the scene --------
cylinder = Cylinder()
cylinder.setDrawer(drawer)
cylinder.create(scanAngle=30) # subdivision

mainScene.addShape("cylinder", cylinder)
# ------------------ end ---------------------------

# ----------- Choose active camera for the view ----------
mainScene.selectCamera("mainCamera")
# --------------- end ---------------------


def main():
	mainWindow = InteractiveWindow("App", 800, 600)
	# ---------- set mainScene as the window display source
	mainWindow.setScene(mainScene)
	# --------------- end --------------------------

	# ----------- make some arrangement to fit the screen ------
	mainWindow.getScene().linearMoveShapeto("box", -4, 0, 0, tranformationSpace=Space.SCENE) # in scene space
	mainWindow.getScene().linearMoveShapeto("cylinder", 4, 0, 0) # in scene space
	# -------------------- end ----------------------

	# ---------Print usage to the terminal------
	mainWindow.usage()
	# --------------- end ----------------

	# ----------- start the window --------------
	mainWindow.run()
	# ---------------- end ----------------------
	
main()

