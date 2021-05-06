def even_odd_appearance_alogrithm():
	"""
	Runs an algorithm that generates 100 random numbers between 0 and 999, checks if the number is even or odd and puts the number in the appropriate part of a dictionary. Calculates how long it will take.
	"""
	from random import randint
	from time import time

	def find_even_odd_appearance(nums):
		evens,odds = [],[]
		d = {}
		for i in nums:
			if i in d.keys(): d[i] += 1
			else: d.update({i:1})
		for k,v in d.items():
			if v % 2 == 0: evens.append(k)
			else: odds.append(k)
		return evens,odds

	def rand_nums(count:int, smallest:int, largest:int):
		while count > 0:
			count -= 1
			yield randint(smallest,largest)
	
	count,mini,maxi = 100, 0, 999

	start = time()
	x = find_even_odd_appearance(rand_nums(count, mini, maxi))
	end = time()

	print(f"Count:     {count:,}\nMin Range: {mini:,}\nMax Range: {maxi:,}\nTime:      {end-start}\n")
	print(f"Evens: {x[0]}\nOdds: {x[1]}")