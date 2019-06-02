from shapes import *

class SubdividerType:
    SIMPLE_SUBDIVIDER = 0
    CATMULL_CLARK_SUBDIVIDER = 1

class Subdivider:

    def __init__(self, shape):
        self._shape = shape
    
    def subdivide(self, indicator="+"):
        pass

    def getShape(self):
        return self._shape