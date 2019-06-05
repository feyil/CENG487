# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

from utils import ColorRGBA
import random

class DrawStyle:
    NODRAW = 0
    SMOOTH = 1
    WIRE = 2
    WIRE_ON_SHADED = 3

class Drawer:
    def __init__(self):
        # protected attributes
        self._verticeList = 0 
        self._faceList = 0
        self._drawStyle = DrawStyle.NODRAW
        
        self._color = None
        self._wireColor = None
        self._wireWidth = 2

    def setDrawStyle(self, drawStyle):
        self._drawStyle = drawStyle

    def setVerticeList(self, verticeList):
        self._verticeList = verticeList
    
    def setFaceList(self, faceList):
        self._faceList = faceList

    def setColor(self, colorRGBA):
        self._color = colorRGBA

    def randomColor(self):
        r = random.uniform(0, 1)
        g = random.uniform(0, 1)
        b = random.uniform(0, 1)

        return ColorRGBA(r, g, b, 0)

    def setWireColor(self, colorRGBA):
        if(colorRGBA == None):
            self._wireColor = ColorRGBA(1, 1, 1, 0)
        else:
            self._wireColor = colorRGBA

    def setWireWidth(self, width):
        if(width == None):
            self._wireWidth = 2
        else:
            self._wireWidth = width

    def draw(self):
        # Inherit and implement
        pass

