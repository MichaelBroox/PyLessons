import math
from math import pi

side = float(input('Enter the side of the Pentagon: \n>>>'))

Area = 5 * side * 4 * math.tan(pi/5)

print('The Area of the Pentagon is: {}'.format(Area))