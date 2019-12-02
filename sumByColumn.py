matrix = [[6,2,3], [4,5,6], [7,8,9]]

totalSum = [sum(i) for i in zip(*matrix)]

print('initial List - ', str(matrix))
print('sum by column - ', str(totalSum))