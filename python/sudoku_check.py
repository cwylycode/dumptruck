def is_sudoku(grid:list):
	'''
	Check if a grid list is a valid sudoku block.
	E.g. - [
		[1,3,2],
		[9,7,8],
		[4,5,6]
	] -> true
	'''
	try: 
		arr = [x for y in grid for x in y]
		if len(arr) != 9: raise Exception
		used = []
		for n in arr:
			if not isinstance(n,int): raise Exception
			if 0 < n < 10:
				if n in used: raise Exception
				else: used.append(n)
			else: raise Exception
	except: return False
	return True