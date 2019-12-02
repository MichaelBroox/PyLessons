from math import pi

raduis = float(input('Enter the raduis value of the cylinder: \n>>>'))
length = float(input('Enter the length of the cylinder: \n>>>'))
area = raduis * raduis * pi
volume = area * length

print('The Area of the cylinder is {}'.format(area))
print('The volume of the cylinder is {}'.format(volume))
