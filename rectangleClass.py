class Rectangle:
	def __init__(self, width, heigth):
		self.__width = width
		self.__heigth = heigth

	def getArea(self):
		area = self.__heigth * self.__width
		return area

	def getPerimeter(self):
		perimeter = 2 * self.__heigth + 2 * self.__width
		return perimeter


perimeter = Rectangle(10, 12)
print ('The Perimeter of the rectangle is: ', perimeter.getPerimeter())
print('The Area of the rectangle is: ', perimeter.getArea())