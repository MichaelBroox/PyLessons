pay = float(input('Enter the value of pay: >>> '))

if pay > 90:
	pay += pay * 0.3
	print(pay)
else:
	pay += pay * 0.1
	print(pay)	