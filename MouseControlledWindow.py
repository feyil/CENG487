from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *
from Window import WindowGL
from Camera import *

from Scene import *

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

        self.usage()
    
    def registerEvents(self):
       glutKeyboardFunc(self.keyPressed)
       glutSpecialFunc(self.specialKeyPressed)
       glutMouseFunc(self.mousePressed )
       glutMotionFunc(self.mouseMove )

    def keyPressed(self, *args):
        if(args[0] == ESCAPE):
            sys.exit()
        elif(args[0] == '+' or args[0] == '-'):
            self.getScene().subdivide("mainShape", args[0])
        elif(args[0] == 'f'):
            camera = self.getScene().getActiveCamera()
            camera.setCameraPosition(0,0,12)
            camera.setWorldUp(0,1,0)
            camera.updateCamera()
    
    def specialKeyPressed(self, *args):
        pass

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
        xSpeed = 0.06
        ySpeed = 0.06
        xOffset = (x - self.mouseX) * xSpeed
        yOffset = (y -self.mouseY)  * ySpeed

        if (self.event.button == GLUT_RIGHT_BUTTON):
			pass
        elif (self.event.button == GLUT_MIDDLE_BUTTON):
            pass
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
                "-> Press f key to reset camera position\n" +
                "-> Press + key to increase subdivision level\n" +
                "-> Press - key to decrease subidivision level\n")  


    def __str__(self):
        return WindowGL.__str__(self)