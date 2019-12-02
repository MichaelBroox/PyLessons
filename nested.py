a = int(input ('Enter an integer value: \n>>> '))
while a != 0:
	if a == 14:
		break
	else:
		b = range(int(input('Enter the lower value of the range: \n>>> ')) - 1, int(input('Enter upper value of the range: \n>>> ')))
		for x in b:
			if (x % 2 == 0):
				print ('{} is even'.format(x))
			else:
				print ('{} not even'.format(x))