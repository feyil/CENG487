# CENG 487 Assignment4 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# June 2019

import sys
from shapes import Shape

class ObjParser:
    
    @staticmethod
    def parse(fileName):
        """
            Use this parser to enable subidivision properly
        """
        # returns shape object
        shape = Shape()

        objFile = open(fileName)

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

    @staticmethod
    def parseMulti(fileName):
        objFile = open(fileName)

        shapeList = []
        vertexCount = 0

        shape = Shape()
        shape.setShapeName("ShortBox")

        for line in objFile:
            splitedLine = line.split()

            if(len(splitedLine) != 0 and splitedLine[0] != '#'):
                definition = splitedLine[0]

                if(definition == 'g' and splitedLine[1] == 'default'):
                    #Start for an object creation
                    shape = Shape()
                elif(definition == 'v'):
                    shape.addVertice(float(splitedLine[1]), float(splitedLine[2]), float(splitedLine[3]))
                    vertexCount += 1
                elif(definition =='f'):
                    shapeFace = []
                    for i in splitedLine[1:]:
                        shapeFace.append((int(i) - 1) - vertexCount)
                    shape.addFace(shapeFace)
                elif(definition == 'g' and splitedLine[1] != 'default'):
                    shape.setShapeName(splitedLine[1])
            elif(len(splitedLine) == 0 and shape != None and shape.getSize() > 0):
                shapeList.append(shape)
           
        shapeList.append(shape)

        return shapeList


if __name__ == "__main__":
    a = ObjParser.parse(sys.argv[1])