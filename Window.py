# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from Sphere import Sphere

class WindowGL:

    def __init__(self, windowName, width, height):
        self.__windowName = windowName
        self.__width = width
        self.__height = height
        self.__scale = float(self.__width) / float(self.__height)

        self.__window = 0
        self.__scene = 0
        

    def setScene(self, scene):
        self.__scene = scene

    def drawScene(self):
        # Configureable via inheritance
        self.__scene.drawGL()

    def registerEvents(self):
        # Configureable via inheritance
        pass
       

    # Use above functions to draw   
    # Below embeded configuration setup goes. 
    
    def run(self):
        self.__initializeWindow()
        self.__window = glutCreateWindow(self.__windowName)

        # Register needed event handlers
        self.registerEvents()
        # End

        # When we are doing nothing, redraw the scene.
        glutIdleFunc(self.__drawGLScene)
        # End
	
	    # Register the function called when our window is resized.
        glutReshapeFunc(self.__resizeGLScene)
        # End

        # Initialize GL
        self.__initializeGL()
        # End

        # Start Event Loop
        glutMainLoop()
        # End

    def __initializeWindow(self):
        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

        glutInitWindowSize(self.__width, self.__height)

        glutInitWindowPosition(0,0)

    def __initializeGL(self):

        # RGBA Background Color
        self.__setBackgroundColor(1, 1, 1, 0.0)
        # End

        # GL Configuration
        glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
        glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
        glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
        # End

        # Reset The Projection Matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()					
        # End

        # Current Matrix Mode
        glMatrixMode(GL_MODELVIEW)
        # End
    
    def __drawGLScene(self):
	    # Clear the screen and the depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        # End

        # Draw scene
        self.drawScene()
        # End

        # Swap buffer
        glutSwapBuffers()
        # End

    def __resizeGLScene(self, Width, Height):
        # Updates size
        self.__width = Width
        self.__height = Height
        # End

        # Prevent A Divide By Zero If The Window Is Too Small 
        if Height == 0:						
	        Height = 1
        # End

        # Reset The Current Viewport And Perspective Transformation
        glViewport(0, 0, Width, Height)		
        self.__setPerspective(45, 0.1, 100)
        # End

        # Current Matrix Mode
        glMatrixMode(GL_MODELVIEW)
        # End

    def __setPerspective(self, fov, zNear, zFar):
        # Reset the Projection Matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # End

        # FOV -> Field of View
        gluPerspective(fov, self.__scale, zNear, zFar)

    def __setBackgroundColor(self, red, green, blue, alpha):
        glClearColor(red, green, blue, alpha)
        
    def __str__(self):
        output = ""
        output += "Window Name: {0}\n".format(self.__windowName) 
        output += " Width: {0}\n Height: {1}\n".format(self.__width, self.__height)
        output += " Scale: {0}\n".format(self.__scale)
        output += " Current Scene: {0}".format(self.__scene)
        return output



if __name__ == "__main__":
    window = WindowGL("App", 640, 480)
    print(window)
    window.run()
    