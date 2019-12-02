class Circle:
	def __init__(self, radius):
		self.__radius = radius

	def getPerimeter(self):
		pi = 3.14
		perimeter = 2 * pi * self.__radius
		return perimeter

perimeter = Circle(10)
print ('The Perimeter of the circle is: ', perimeter.getPerimeter())