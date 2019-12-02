def move_mouse(m, maze, pos):
	if m == 'down':
		pos = pos[0], pos[1] + 1
		return pos
maze = [[0 for x in range(8)] for x in range(8)]
pos = (4,4)
pos = move_mouse('down', maze, pos)
print(pos)