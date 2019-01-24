
#a 0 is no queen and 1 is equal queen
#when the place of the queen atack other queen false and start over


#it will return True if it is possible to place a queen in any given square
def possible(x, y):
	for[a, b] in solution:
	  if y == b:
		return False;
	  if abs(x - a) == ab(y - b):
		return False
			return True



solution = []
tried = []

def solve(x, y=1, n):
	if x < n and y < n:
		if possible(x, y) and [x, y] not in tried:
			solution.append([x, y])
		else:
			return solve(x + 1)
			return solve(x, y + 1)
		elif y > n:
			for [c, d] in tried[:]:
				if solution[x - 2][0] < c:
					tried.remove([c, d])
					tried.append(solution[x - 2])
					solution.remove(solution[x - 2])
				return solve(x - 1)
		else:
			print solution
