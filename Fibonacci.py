def recFib(n):
	if n <= 1:
		return n
	else:
		return(recFib(n-1) + recFib(n-2))

nterms = int(input('Enter how many the terms: >>> '))

if nterms <= 0:
	print('Please enter a positive integer')
else:
	print('Fibonacci sequence:')
	for i in range(nterms):
		print(recFib(i))