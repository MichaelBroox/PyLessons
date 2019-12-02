a = range(int(input('Enter the lower value of the range: \n>>> ')) - 1, int(input('Enter upper value of the range: \n>>> ')))
for x in a:
	if (x % 2 == 0):
		print ('{} is even'.format(x))
	else:
		print ('{} not even'.format(x))