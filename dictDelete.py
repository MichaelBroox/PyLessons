dictStudents = {'Ayo' : 24, 'Ade' : 23, 'Emeka' : 20, 'Ephiram' : 26, 'Joseph' : 19}

dictStudents['Steph'] = 30
dictStudents['Kelechi'] = 17

print('Before deleting Steph')
print(dictStudents)
print()

del dictStudents['Steph']

print('After deleting Steph')
print(dictStudents)