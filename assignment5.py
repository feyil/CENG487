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
from materials import *
from lights import *

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
camera.setCameraPosition(0,25,100)
camera.setWorldUp(0,1,0)
camera.linearMove(CamMovement.FORWARD, 0.001) # little trick to focus the target point
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
fileName = sys.argv[1]

objDrawer = ObjDrawer()
shapeList = ObjParser.parseMulti(fileName)



for shape in shapeList:
	name = shape.getShapeName()
	shape.setDrawer(objDrawer)

	if(name == "ShortBox"):
		shape.setColor(0.5,0.5,0.5,0)
		shape.setMaterial(Material(**MaterialDefs.YELLOW_PLASTIC))
	elif(name == "TallBox"):
		shape.setColor(0.5,0.5,0.5,0)
		shape.setMaterial(Material(**MaterialDefs.YELLOW_PLASTIC))
	elif(name ==  "Floor"):
		shape.setColor(0.9,0.9,0.9,0)
		shape.setMaterial(Material(**MaterialDefs.WHITE_PLASTIC))
	elif(name == "Ceiling"):
		shape.setColor(0.9,0.9,0.9,0)
		shape.setMaterial(Material(**MaterialDefs.WHITE_PLASTIC))
	elif(name == "LeftWall"):
		shape.setColor(1,0,0,0)
		shape.setMaterial(Material(**MaterialDefs.RED_PLASTIC))
	elif(name == "RightWall"):
		shape.setColor(0,1,0,0)
		shape.setMaterial(Material(**MaterialDefs.GREEN_PLASTIC))
	elif(name == "BackWall"):
		shape.setColor(1,1,1,0)
		shape.setMaterial(Material(**MaterialDefs.WHITE_PLASTIC))

	mainScene.addShape(name, shape)

dicLight = {
	"lightName": "Directional Light",
	"lightNum": 0,
	"ambient": [0.5, 0.5, 0.5, 1],
	"diffuse": [1, 1, 1, 1],
	"specular": [0.3, 0.3, 0.3, 1],
	"position": [0,48, 0],
}

spotLight = {
	"lightName": "SpotLight",
	"lightNum": 1,
	"ambient": [0.5, 0.5, 0.5, 1],
	"diffuse": [1, 1, 1, 1],
	"specular": [0.3, 0.3, 0.3, 1],
	"position": [-10, 10, 20],
	"cutoff": 45,
	"direction": [0,2,-1,0],
	"exponent": 10
}


light1 = PointLight(**dicLight)
light2 = SpotLight(**spotLight)
mainScene.addLight(light1)
mainScene.addLight(light2)
mainScene.lightsON()


# for shape in shapeList:
	
# 	shape.setDrawer(objDrawer)
# 	shape.setSubdivider(SubdividerType.CATMULL_CLARK_SUBDIVIDER)
# 	shape.setColor(1,1,0,0)
# 	shape.setWireColor(1,0,0,0)
# 	mainScene.addShape(shape.getShapeName(), shape)

# legacy = LegacyDrawer()
# box = Box()
# box.setDrawer(legacy)
# box.create()
# mainScene.addShape("box", box)
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

