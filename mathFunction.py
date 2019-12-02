import math

a = float(input('Enter the first vertice of the triangle: \n>>> '))
b = float(input('Enter the second vertice of the triangle: \n>>> '))
c = float(input('Enter the third vertice of the triangle: \n>>> '))


x = (a*a - b*b - c*c) / (-2 * b * c)
A = math.acos(x)
print('The angle of the Triangle is: {}'.format(A))
