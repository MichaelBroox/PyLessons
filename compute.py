a = float(input('Enter first value: \n>>> '))
b = float(input('Enter second value: \n>>> '))
c = float(input('Enter third value: \n>>> '))

a = a**b
b = b**c

if (a > b and a > c):
	maximum = a
elif (b > a and b > c):
	maximum = b
else:
	maximum = c

print('The maximum number is: {}'.format(maximum))