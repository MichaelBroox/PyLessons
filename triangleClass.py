class Triangle:
    def __init__(self, side1, side2, base):
        self.side1 = side1
        self.side2 = side2
        self.base = base

        if side1 is None:
            self.side1 = 1.0
        else:
            self.side1 = side1
        
        if side2 is None:
            self.side2 = 1.0
        else:
            self.side2 = side2

        if base is None:
            self.base = 2.0
        else:
            self.base = base


    def getArea(self, height):
        #height = float(input('Enter the height of this triangle: >>> ')
        area = 0.5 * self.base * height
        return area


    def getPerimeter(self):
        P = self.side1 + self.side2 + self.base
        return P
    
    def _str_(self):
        return 'Triangle: side1 = ' + str(self.side1) + 'side2 = ' + str(self.side2) + 'base = ' + str(self.base)