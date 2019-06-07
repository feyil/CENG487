# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *
from Window import WindowGL

from cameras import Camera,CamMovement
from drawers import Drawer, DrawStyle
from scenes import Scene, Space

from lights import Light

import math

ESCAPE = '\033'

class Event:
	def __init__(self):
		self.x = -1
		self.y = -1
		self.button = -1
		self.state = -1
		self.altPressed = False


class MouseControlledWindow(WindowGL):

    def __init__(self, windowName, width, height):
        WindowGL.__init__(self, windowName, width, height)

        self.event = Event()
        self.mouseX = -1
        self.mouseY = -1

        self.moveLight = False
        self._proceduralSutffArgs["angle"] = 0

        self.usage()
    
    def registerEvents(self):
       glutKeyboardFunc(self.keyPressed)
       glutSpecialFunc(self.specialKeyPressed)
       glutMouseFunc(self.mousePressed)
       glutMotionFunc(self.mouseMove)

    def keyPressed(self, *args):
        if(args[0] == ESCAPE):
            sys.exit()
        elif(args[0] == '+' or args[0] == '-'):
            self.getScene().subdivide("mainShape", args[0])
        elif(args[0] == 'f'):
            camera = self.getScene().getActiveCamera()
            camera.setCameraPosition(0,25,120)
            camera.setWorldUp(0,1,0)
            camera.linearMove(CamMovement.FORWARD, 0.001) # little trick to focus the target point
            camera.updateCamera()
        elif(args[0] == '4'):
            self.getScene().setDrawStyle(DrawStyle.WIRE)
        elif(args[0] == '5'):
            self.getScene().setDrawStyle(DrawStyle.SMOOTH)
        elif(args[0] == '6'):
            self.getScene().setDrawStyle(DrawStyle.WIRE_ON_SHADED)
        elif(args[0] == 'q'):
            if(self.getScene().getLightsStatus()):
                self.getScene().lightsON(False)
            else:
                self.getScene().lightsON(True)
        elif(args[0] == 'w'):
            self.controlLight(0)
        elif(args[0] == 'e'):
            self.controlLight(1)
        elif(args[0] == "a"):
            light = self.getScene().getLight(Light.LIGHT_NUM[0])
            if(not self.moveLight):
                self.moveLight = True
            else:
                self.moveLight = False
    
            self._proceduralSutffArgs["light"] = light
            #self._proceduralSutffArgs["angle"] = 0

    def calculateRadian(self, degree):
        return float(degree) * (math.pi / 180)  
            
    # override from WindowGL
    def proceduralStuff(self):
        if(self.moveLight):
            self._proceduralSutffArgs["angle"] += self.calculateRadian(1)
            degree = self._proceduralSutffArgs["angle"]
            self._proceduralSutffArgs["light"].updatePosition(math.cos(degree)* 0.5,0,math.sin(degree)* 0.5)


    def controlLight(self, lightNum):
        scene = self.getScene()
        if(scene.getLightStatus(Light.LIGHT_NUM[lightNum])):
            scene.lightON(Light.LIGHT_NUM[lightNum], False)
        else:
            scene.lightON(Light.LIGHT_NUM[lightNum], True)
          
    
    def specialKeyPressed(self, *args):
        scene = self.getScene()
        shapeName = "mainShape"
        scanAngle = 10

        if(args[0] == GLUT_KEY_LEFT):
            scene.rotateMoveShapeTo(shapeName, -scanAngle, "Y", Space.LOCAL)
        elif(args[0] == GLUT_KEY_RIGHT):
            scene.rotateMoveShapeTo(shapeName, scanAngle, "Y", Space.LOCAL)
        elif(args[0] == GLUT_KEY_UP):
            scene.rotateMoveShapeTo(shapeName, scanAngle, "X", Space.LOCAL)
        elif(args[0] == GLUT_KEY_DOWN):
            scene.rotateMoveShapeTo(shapeName, -scanAngle, "X", Space.LOCAL)

    def mousePressed(self, button, state, x, y):
        self.event.x = x   
        self.event.y = y
        self.event.state = state
        self.event.button = button

		# get status of alt key
        m = glutGetModifiers()
        self.event.altPressed = m & GLUT_ACTIVE_ALT

        self.mouseX = x
        self.mouseY = y

        self.rotated = 0

    def mouseMove(self, x, y):
        camera = self.getScene().getActiveCamera()

       	if self.event.altPressed == False:
			return
        xSpeed = 0.3
        ySpeed = 0.3
        xOffset = (x - self.mouseX) * xSpeed
        yOffset = (y -self.mouseY)  * ySpeed

        acelerationFactor = 2
        if (self.event.button == GLUT_RIGHT_BUTTON):
            if(xOffset > 0):
                camera.linearMove(CamMovement.FORWARD, xSpeed * acelerationFactor)
            else:
                camera.linearMove(CamMovement.BACKWARD, xSpeed * acelerationFactor)
        elif (self.event.button == GLUT_MIDDLE_BUTTON):
            if(xOffset > 0):
                camera.linearMove(CamMovement.LEFT, xSpeed)
            else:
                camera.linearMove(CamMovement.RIGHT, xSpeed)

            if(yOffset > 0):
                camera.linearMove(CamMovement.UP, ySpeed)
            else:
                camera.linearMove(CamMovement.DOWN, ySpeed) 
        elif (self.event.button == GLUT_LEFT_BUTTON):
            camera.rotateCamera(yOffset, axis="X")
            camera.rotateCamera(xOffset, axis="Y")
         
		# store last positions
        self.mouseX = x
        self.mouseY = y

		# remember this point
        self.event.x = x
        self.event.y = y 

    def usage(self):
        print("------------------------ KEY CONFIGURATION ------------------------\n" +
                "-> Press ESC to quit\n" +
                "-> CRTL + ALT + MOUSE LEFT BUTTON and move mouse to rotate camera\n" +
                "-> CRLT + ALT + MOUSE MIDDLE BUTTON and move mouse to move target\n" +
                "-> CRLT + ALT + MOUSE RIGHT BUTTON and move mouse to zomm in and out\n" +
                "-> Press f key to reset camera position\n" +
                "-> Press 4 to draw WIRES\n" +
                "-> Press 5 to draw SMOOTH\n" +
                "-> Press 6 to draw WIRE ON SHADED\n" +
                "-> Press q to on/off GL_LIGHTING\n" +
                "-> Press w to on/off LIGHT0\n" + 
                "-> Press e to on/off LIGHT1\n" +
                "-> Press a to start/stop procedural movement of light")  


    def __str__(self):
        return WindowGL.__str__(self)