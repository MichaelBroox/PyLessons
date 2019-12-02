def power(x, y):
	if y == 0:
		return 1

	if y >= 1:
		return x*power(x, y-1)

base = int(input('Enter the base number: >>> '))

exp = int(input('Enter the number of the exponent: >>> '))

Expo = power(base, exp)

print('{} raised to the power {} is: {}'.format(base, exp, Expo))