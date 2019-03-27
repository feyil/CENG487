from Shape import Shape

class Torus(Shape):

    def __init__(self):
        Shape.__init__(self)

    def draw(self):
        print("Draw Torus")

    def __str__(self):
        return Shape.__str__(self)
        

a = Torus()
print(a)
