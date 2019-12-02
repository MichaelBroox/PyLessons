accepted_digits = list(range(0, 1001))

digit = int(input('Enter an integer value (0 - 1000) to calculate the sum of it: \n>>> '))

Sum = 0

if digit in accepted_digits:
	while(digit != 0):
		Sum = Sum + (digit % 10)
		digit = digit // 10
	print ('The sum of the digits of the integer value you entered is {}'.format(Sum))
else:
	print('The value you entered is not withing the range (0 - 1000)')



