List = list(range(int(input('Create a list... \nEnter the lower value of the range: \n>>> ')), int(input('Enter upper value of the range: \n>>> '))))
for val in List:
	if val > 1:
		for n in range(2, val):
			if (val % n == 0):
				break
		else:
			print(val)