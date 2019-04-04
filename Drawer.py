# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019

# It is an idea later I will consider detailedly
# I am thinking on strategy design pattern

class Drawer:

    def __init__(self):
        # protected attributes
        self._verticeList = 0 
        self._faceList = 0

    def setVerticeList(self, verticeList):
        self._verticeList = verticeList
    
    def setFaceList(self, faceList):
        self._faceList = faceList

    def draw(self):
        # Inherit and implement
        pass

