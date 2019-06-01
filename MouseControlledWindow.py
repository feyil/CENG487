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
        if args[0] == ESCAPE:
            sys.exit()
    
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

    def mouseMove(self, x, y):
        camera = self.getScene().getActiveCamera()

       	if self.event.altPressed == False:
			return

        xOffset = (x - self.mouseX)
        yOffset = (y -self.mouseY)

        if (self.event.button == GLUT_RIGHT_BUTTON):
			pass
        elif (self.event.button == GLUT_MIDDLE_BUTTON):
            pass
        elif (self.event.button == GLUT_LEFT_BUTTON):
            camera.rotateMove(xOffset, yOffset)

		# store last positions
        self.mouseX = x
        self.mouseY = y

		# remember this point
        self.event.x = x
        self.event.y = y 

    def usage(self):
        pass

    def __str__(self):
        return WindowGL.__str__(self)