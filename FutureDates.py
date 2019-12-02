days = ['Sunday', 'Monday', 'Tuesday', 'Wednessday', 'Thurday', 'Friday', 'Saturday']

todayDate = int(input('Enter an integer for today\'s day of the week from 0 - 6, Sunday is 0 and Saturday is 6: \n>>> '))

print('Today is {}'.format(days[todayDate]))

futureDate = int(input('Enter the number of days after today: \n>>> '))

print('The future day is: {} '.format(days[(todayDate+futureDate) % 7]))