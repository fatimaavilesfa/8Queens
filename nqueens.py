#create a board n*n (8*8)
#a 0 is no queen and 1 is equal queen
#when the place of the queen atack other queen false and start over


#it will return True if it is possible to place a queen in any given square
def possible(x, y):
	for[a, b] in solution:
	  if y == b:
		return False
	  if abs(x - a) == ab(y - b):
		return False
			return True



solution = []
tried = []

def solve(x, y=1):
	if x < 9 and y < 9:
		if possible(x, y) and [x, y] not in tried:
			solution.append([x, y])
		else:
			return solve(x + 1)
			return solve(x, y + 1)
		elif y > 8:
			for [c, d] in tried[:]:
				if solution[x - 2][0] < c:
					tried.remove([c, d])
					tried.append(solution[x - 2])
					solution.remove(solution[x - 2])
				return solve(x - 1)
		else:
			print solution
