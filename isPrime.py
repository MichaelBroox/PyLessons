def checker(value):
	if value <= 1:
		return False
	for i in range (2, value):
		if value % i == 0:
			return False
	return True

def isPrime(n):
	#n = int(input('Enter value to check if it is a Prime number or not: \n>>> '))
	if checker(n):
		print(n, 'is prime.')
	else:
		print(n, 'is not prime.')

prime = isPrime(13)