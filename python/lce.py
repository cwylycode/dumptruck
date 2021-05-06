def longest_common_end(strings:list):
	"""
	Finds the longest substring from the end of each string that all match and returns that substring.
	"""
	common = ""
	for string in strings:
		string = "".join(reversed(string.lower()))
		x = []
		if not common:
			common = string
			continue
		for i,s in enumerate(string):
			try:
				if s == common[i]: x.append(s)
				else: break
			except: break
		common = "".join(x)
		if not common: return ""
	return "".join(reversed(common))

if __name__ == "__main__":
	s = [
		"penny",
		"canny",
		"sunny",
		"funny"
	]
	print(f"Words: {s}\n")
	print(f"Longest Common End: {longest_common_end(s)}")
	input()