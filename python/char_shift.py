def shift_characters(chars:str,shift:list) -> str:
	"""
	Shift the characters up or down in their ascii values by the number in each array element. Elements must be ints and array must be same length as string.
	"""

	string = []
	for i,s in enumerate(chars):
		string.append(chr(ord(s)+shift[i]))
	return "".join(string)