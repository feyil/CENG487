# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019

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
        self._wireWidth = 2

    def setDrawStyle(self, drawStyle):
        self._drawStyle = drawStyle

    def setVerticeList(self, verticeList):
        self._verticeList = verticeList
    
    def setFaceList(self, faceList):
        self._faceList = faceList

    def draw(self):
        # Inherit and implement
        pass

