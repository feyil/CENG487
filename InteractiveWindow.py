# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# March 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import fonts
from OpenGL.GLX import c_void_p

from OpenGL.GLU import *

from Window import WindowGL
from Camera import *

from Scene import *





# Note local space rotation causes scene space movement to rotate shape small amount
# I will find it later probably local space rotation reflect to scene space final matrix and cause rotation 

# ------------------------ KEY CONFIGURATION ------------------------
# 1 -> switch mainCamera
# 2 -> switch cam2
# 3 -> selected camera free move
#   -> w -> in
#   -> s -> out
#   -> a -> right
#   -> d -> left
#   -> e -> up
#   -> r -> down
#   -> up -> pitch up
#   -> down -> pitch down
#   -> left -> yaw left
#   -> right -> yaw right
# 4 -> select box
# 5 -> select sphere
# 6 -> select cylinder
# + -> increase subdivision for selected shape
# - -> decrease subidivison for selected shape
# Select a shape and move using
#   Scene Space
#       -> w -> up
#       -> s -> down
#       -> a -> left
#       -> d -> right
#       -> e -> in
#       -> r -> out
#   Local Space
#       -> up 
#       -> down
#       -> left
#       -> right
# Rotation of selected shape
#   -> k -> scene space use x, y, z button to rotate
#   -> l -> local space use x, y, z button to rotate
# -------------------------- END ---------------------------------------

class InteractiveWindow(WindowGL):

    def __init__(self, windowName, width, height):
        WindowGL.__init__(self, windowName, width, height)
        self.__selected = 0
        self.__space = 0

    def registerEvents(self):
        glutKeyboardFunc(self.processKey)
        glutSpecialFunc(self.processKey)

    def processKey(self, *args):
        key = args[0]
       
        if(key == '1'):
            self.getScene().selectCamera("mainCamera")
        elif(key == '2'):
            self.getScene().selectCamera("cam2")
        
        if(self.__selected == '3' or key == '3'):
            # Free move with the camera
            if(self.__selected != '3'):
                self.__selected = key
            
            self.camFreeMove(args)
        if(self.__selected == '4' or key == '4'):
            # Box selected
            if(self.__selected != '4'):
                self.__selected = key
            
            self.subdivideKey("box", args)
            self.shapeMovement("box", args)
        if(self.__selected == '5' or key == '5'):
            # Sphere selected
            if(self.__selected != '5'):
                self.__selected = key

            self.subdivideKey("sphere", args)
            self.shapeMovement("sphere", args)
        if(self.__selected == '6' or key == '6'):
            # Cylinder selected
            if(self.__selected != '6'):
                self.__selected = key

            self.subdivideKey("cylinder", args)
            self.shapeMovement("cylinder", args)
            
    def subdivideKey(self, shapeName, args):
        key = args[0]

        if(key == '+'):
            self.getScene().subdivide(shapeName, key)
        elif(key == '-'):
            self.getScene().subdivide(shapeName, key)

    def shapeMovement(self, shapeName, args):
        # Shape movement implementation
        scene = self.getScene()
        
        key = args[0]
        
        # Scene space movement
        if(key == 'w'):
            # Up
            scene.linearMoveShapeto(shapeName, 0, 1, 0)
        elif(key == 's'):
            # Down
            scene.linearMoveShapeto(shapeName, 0, -1, 0)
        elif(key == 'a'):
            # Left
            scene.linearMoveShapeto(shapeName, -1, 0, 0)
        elif(key == 'd'):
            # Right
            scene.linearMoveShapeto(shapeName, 1, 0, 0)
        elif(key == 'e'):
            # In
            scene.linearMoveShapeto(shapeName, 0, 0, 1)
        elif(key == 'r'):
            # Out
            scene.linearMoveShapeto(shapeName, 0, 0, -1)
        
        # Local space movement
        # Arrow buttons
        if(key == 101):
            # Up
            scene.linearMoveShapeto(shapeName, 0, 1, 0, Space.LOCAL)
        elif(key == 103):
            # Down
            scene.linearMoveShapeto(shapeName, 0, -1, 0, Space.LOCAL)
        elif(key == 100):
            # Left
            scene.linearMoveShapeto(shapeName, -1, 0, 0, Space.LOCAL)
        elif(key == 102):
            # Right
            scene.linearMoveShapeto(shapeName, 1, 0, 0, Space.LOCAL)

        # Local and Scene movement
        if(self.__space == Space.LOCAL or key == 'l'):
            if(key == 'l'): # local space
                self.__space = Space.LOCAL
            if(key == 'x'): # rotate around x
                scene.rotateMoveShapeTo(shapeName, 10, "X", self.__space)
            elif(key == 'y'): # rotate around y
                scene.rotateMoveShapeTo(shapeName, 10, "Y", self.__space)
            elif(key == 'z'): # rotate around z
                scene.rotateMoveShapeTo(shapeName, 10, "Z", self.__space)
        if(self.__space == Space.SCENE or key == 'k'):
            if(key == 'k'): # scene space
                self.__space = Space.SCENE
            if(key == 'x'): # rotate around x
                scene.rotateMoveShapeTo(shapeName, 10, "X", self.__space)
            elif(key == 'y'): # rotate around y
                scene.rotateMoveShapeTo(shapeName, 10, "Y", self.__space)
            elif(key == 'z'): # rotate around z
                scene.rotateMoveShapeTo(shapeName, 10, "Z", self.__space)
            
    def camFreeMove(self, args):
        # Camera free move implementation
        
        camera = self.getScene().getActiveCamera()

        key = args[0]
        speed = 1

        if(key == 'w'):
            # Forward
            camera.linearMove(CamMovement.FORWARD, speed)
        elif(key == 's'):
            # Backward
            camera.linearMove(CamMovement.BACKWARD, speed)
        elif(key == 'a'):
            # Left
            camera.linearMove(CamMovement.LEFT, speed)
        elif(key == 'd'):
            # Right
            camera.linearMove(CamMovement.RIGHT, speed)
        elif(key == 'e'):
            # Up
            camera.linearMove(CamMovement.UP, speed)
        elif(key == 'r'):
            # Down
            camera.linearMove(CamMovement.DOWN, speed)
        
        if(key == 101): # UP pitch
            camera.rotateMove(0,-100)
        elif(key == 103 ): # DOWN pitch
            camera.rotateMove(0,100)
        elif(key == 100): # left yaw
            camera.rotateMove(100,0)
        elif(key == 102): # rigth yaw
            camera.rotateMove(-100,0)

    def usage(self):
        print("------------------------ KEY CONFIGURATION ------------------------\n" +
                "1 -> switch mainCamera\n" +
                "2 -> switch cam2\n" +
                "3 -> selected camera free move\n" +
                "     -> w -> in\n" +
                "     -> s -> out\n" +
                "     -> a -> right\n" +
                "     -> d -> left\n" +
                "     -> e -> up\n" +
                "     -> r -> down\n" +
                "     -> up -> pitch up\n" +
                "     -> down -> pitch down\n" +
                "     -> left -> yaw left\n" +
                "     -> right -> yaw right\n" +
                "4 -> select object\n" +
                "(Not Valid)5 -> select sphere\n" +
                "(Not Valid)6 -> select cylinder\n" +
                "+ -> increase subdivision for selected shape\n" +
                "- -> decrease subidivison for selected shape\n" +
                "Select a shape and move using\n" +
                " Scene Space\n" +
                    "     -> w -> up\n" +
                    "     -> s -> down\n" +
                    "     -> a -> left\n" +
                    "     -> d -> right\n" +
                    "     -> e -> in\n" +
                    "     -> r -> out\n" +
                " Local Space\n" +
                "     -> up\n" +
                "     -> down\n" +
                "     -> left\n" +
                "     -> right\n" +
                "Rotation of selected shape\n" +
                " -> k -> scene space use x, y, z button to rotate\n" +
                " -> l -> local space use x, y, z button to rotate\n" +
                "-------------------------- END ---------------------------------------")
    def __str__(self):
        return WindowGL.__str__(self)

if __name__ == "__main__":
    a = InteractiveWindow("a", 800, 600)
    a.usage()    