number = int(input('Enter a three digit number: >>> '))

n = number
reverse = 0

while number>0:
	digit = number%10
	reverse = reverse*10+digit
	number = number//10
if n == reverse:
	print('Yea it is Palindrome')
else:
	print('Not Palindrome')