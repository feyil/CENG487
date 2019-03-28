# CENG 487 Assignment1 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from Vec3d import Vec3d
from Mat3d import Mat3d
from Shape import Shape
from Sphere import Sphere
from Cylinder import Cylinder
from Camera import Camera
from Box import Box


import time
import math
import random

x = 0
y = 0
z = 1
camera = 0
triangle = 0
square = 0
degree = 0
angle = 0

# for keystrokes
square = 0
triangle = 0
ESCAPE = '\033'
rot = 0.0
# Number of the glut window.
window = 0



# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(1, 1, 1, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
	# 									# Calculate The Aspect Ratio Of The Window
    # gluPerspective(60, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
	

# The main drawing function. 
def DrawGLScene():
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 
	
	glTranslate(0,0,-6)
	# Draw a square start
	          # Bluish shade

	global angle
	drawQuad(square)                          # We are done with the polygon
	# drawQuad(triangle)
	# square.transformShape(b)


	#  since this is double buffered, swap the buffers to display what just got drawn. 
	glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	print(args)

def drawQuad(square):
	glBegin(GL_QUADS)
	color = 0
	for i in square.getShape():
		color += 1
		if(color % 2 == 0):
			glColor3f(0.8, 0.3, 0.8)
		else:
			glColor3f(0.2, 0.8, 0.3)
		glVertex3f(i.getX(), i.getY(), i.getZ())
	glEnd()             

def main():
	global window
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	glutInitWindowSize(640, 480)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("Furkan Emre YILMAZ")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc(DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
	
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)
	
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)

	# Initialize our window. 
	InitGL(640, 480)
	glutSpecialFunc(specialKey)
	# Start Event Processing Engine	
	glutMainLoop()
	
def specialKey(*args):
	print("PUSH")
	global x,y,z,triangle, square, degree
	if(args[0] == GLUT_KEY_UP):
		print("UP")
		degree += 5
	elif(args[0] == GLUT_KEY_DOWN):
		print("DOWN")
		degree -=  5
	elif(args[0] == GLUT_KEY_RIGHT):
		z += 0.5
	elif(args[0] == GLUT_KEY_LEFT):
		z -= 0.5
	elif(args[0] == GLUT_KEY_F1):
		print("F1")

	radian = degree * (math.pi / 180)
	x = 1 * math.cos(radian)
	y = 1 * math.sin(radian)

	camera.setCameraPosition(x,y,z)
	# camera.setWorldUpVector(0,1,z - 1)
	camera.setWorldUpVector(-math.sin(radian),math.cos(radian),0)
	camera.loadCamera()
	square = camera.lookAt(s)
	triangle = camera.lookAt(t)
	DrawGLScene()


	
# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")


# Square Start
s = Shape()

# Start from left top and continue counter clockwise
s.addVertice(1,1,0)
s.addVertice(-1,1,0)
s.addVertice(-1,-1,0)
s.addVertice(1,-1,0)


# Calculate angle to rotate for a quad to match one edge
r = 1 # radius
hipotenous = math.sqrt((r * r) + 1)
print(hipotenous)
half_angle_radian = math.acos(r / hipotenous)
angle = 2 * (half_angle_radian * 180 / math.pi)
# end angle calculation

print(angle)

s.transformShape(Mat3d().defineTranslationMatrix(0,0,r))
t = s.clone().transformShape(Mat3d().defineRotationMatrix(angle, "X"))

camera = Camera()

radian = 0 * (math.pi / 180)

x,y,z = 0, 0, -1

s = Cylinder()
s.drawCylinder()


camera.setCameraPosition(0, 0, z)
camera.setTargetPosition(0,0,0)
camera.setWorldUpVector(0,1,0)

camera.loadCamera()
square = camera.lookAt(s)
triangle =camera.lookAt(t)

#print(s)
main()
    	
