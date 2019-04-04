# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019

from OpenGL.GL import *

from Drawer import Drawer


class ObjDrawer(Drawer):

    def __init__(self):
        Drawer.__init__(self)

    def draw(self):
        print("Draw")