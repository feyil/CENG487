# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *
import sys
from PIL import Image

import numpy as np

class WindowGL:

    def __init__(self, windowName, width, height):
        self.__windowName = windowName
        self.__width = width
        self.__height = height
        self.__scale = float(self.__width) / float(self.__height)

        self.__window = 0
        self.__scene = 0

        self.__drawingState = True

        self._proceduralSutffArgs = {}

        self._shadow = None

    def setDrawingState(self, state):
        self.__drawingState = state

    def getDrawingState(self):
        return self.__drawingState

    def setScene(self, scene):
        self.__scene = scene

    def getScene(self):
        return self.__scene

    def drawScene(self):
        # Run procedural things
        self.proceduralStuff()

        # Configureable via inheritance
        self.__scene.draw()

    def setShadow(self, shadow):
        self._shadow = shadow

    def initializeShadow(self):
        if(self._shadow != None):
            self._shadow.initializeShadowComponents()

    def registerEvents(self):
        # Configureable via inheritance
        pass

    # Override and implement
    def proceduralStuff(self):
        # I prefer to use seperate thread but I am not sure
        # you have that lib or not
        pass


    # Use above functions to draw   
    # Below embeded configuration setup goes. 
    
    def run(self):
        self.__initializeWindow()
        self.__window = glutCreateWindow(self.__windowName)

        # initialize shadow components
        self.initializeShadow()        
        
        # Register needed event handlers
        self.registerEvents()
        # End

        # When we are doing nothing, redraw the scene.
        glutIdleFunc(self.__drawGLScene)
        # End
        
        # Set glut display function
        glutDisplayFunc(self.__drawGLScene)

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
        self.__setBackgroundColor(0, 0, 0, 0.0)
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
        if(self.getDrawingState()):

            shadow = self._shadow

            shadow.renderDepthMap(self.__scene)

            shadow.bindFBO(True)

            buffer = ( GLulong * (1*800*600) )(0)
            glReadPixels(0, 0, 800, 600, GL_DEPTH_COMPONENT, GL_FLOAT, buffer)
            depth_data = np.fromstring(buffer, dtype=np.float32)

            shadow.bindFBO(False)

            # Use PIL to convert raw RGB buffer and flip the right way up
            image = Image.frombytes(mode="L", size=(800, 600), data=depth_data)     
            image = image.transpose(Image.FLIP_TOP_BOTTOM)

            # Save image to disk
            image.save('jpap.png')
         
            # Clear the screen and the depth buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            # End

            # draw the scene
            self.drawScene()
          
            # Swap buffer
            glutSwapBuffers()
            # End

            #exit()
        else:
            glLoadIdentity()
            glutSwapBuffers()

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
        self.__setPerspective(45, 0.1, 300)
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
    