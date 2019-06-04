# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

import sys
from shapes import Shape

class ObjParser:
    # Will create a shape object at the end of parse operation
    def __init__(self, fileName):
        self.__fileName = fileName

    def parse(self):
        # returns shape object
        shape = Shape()

        objFile = open(self.__fileName)

        for line in objFile:
            splitedLine = line.split()
            
            if(len(splitedLine) != 0 and splitedLine[0] != '#'):
                definition = splitedLine[0]
                
                if(definition == 'o'):
                    shape.setShapeName(splitedLine[1])
                elif(definition == 'v'):
                    shape.addVertice(float(splitedLine[1]), float(splitedLine[2]), float(splitedLine[3]))
                elif(definition == 'f'):
                    face = []
                    for i in splitedLine[1:]:
                        face.append(int(i) - 1)
                    shape.addFace(face)
    
        return shape
                

if __name__ == "__main__":
    a = ObjParser(sys.argv[1])
    a.parse()