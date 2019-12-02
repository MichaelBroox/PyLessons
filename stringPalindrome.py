
valString = input('Enter a word to check if it is a palindrome or not: \n>>> ')

isPalindrome = True

for i in range(0, len(valString) // 2):
	if valString[i] != valString[len(valString) - i -1]:
		isPalindrome = False

if isPalindrome:
	print(valString, 'is a Palindrome')
else:
	print(valString, 'is not Palindrome')