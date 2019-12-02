import random
List9 = [[6,6,7,8,9], [0,9,8,6,7], [0,8,0]]
for row in range(len(List9)):
	for column in range(len(List9[row])):
		i = random.randint(0, len(List9) - 1)
		j = random.randint(0, len(List9[row]) - 1)
		List9[row][column], List9[i][j] = List9[i][j], List9[row][column]

		print(List9)
