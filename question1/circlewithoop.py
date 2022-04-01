from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius ** 2 * pi

    def getPerimeter(self):
        return self.radius * 2 * pi

circo = Circle(20)