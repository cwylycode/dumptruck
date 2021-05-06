def find_boomerangs(nums:list):
	"""
	Provide a list of numbers(count > 2) to check for any 'boomerangs' in the sequence. A boomerang is any 3 numbers in a row that are the same value at both ends, but different in the middle number.\n
	E.g. - (3,5,3)(true), (6,3,2)(false), (9,2,9)(true), (4,4,4)(false), (7,7,6)(false), (1,2,1)(true)
	"""
	boomerangs = []
	end = len(nums)-1
	last = 2
	if last > end: return []
	while last <= end:
		if nums[last] == nums[last-2]:
			if nums[last-1] != nums[last]:
				boomerangs.append(nums[last-2:last+1])
		last += 1
	return boomerangs

if __name__ == "__main__":
	numbers = [666,777,666,69,69,7,69,7]
	print("Numbers: ",numbers,'\n')
	print(find_boomerangs(numbers))