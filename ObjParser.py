# CENG 487 Assignment2 by
# Furkan Emre Yilmaz
# StudentId: 230201057
# April 2019

import sys
from Shape import Shape

class ObjParser:
    # Will create a shape object at the end of parse operation
    def __init__(self):
        print("ObjParse")
        self.__shape = Shape()

    def parse(self, fileName):
        # returns shape object
        print("Parse")



if __name__ == "__main__":
    a = ObjParser()
    print(sys.argv)