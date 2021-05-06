# Same as secret password function in C++, but this only took 30 mins and the other took hours. Gahd.
import string

def secret_password(s:str):
	"""
	Create a secret password - must be exactly 9 characters long (letters only) or you get shot to death.
	"""
	# Validate
	msg = "BANG! BANG! BANG!"
	if len(s) != 9: return msg
	for x in s:
		if x not in string.ascii_lowercase:
			return msg
	# Split
	sx = [s[i:i+3] for i in range(0,9,3)]
	# Part1 - first and third letter become alphabet nums
	sx[0] = "".join([str(ord(sx[0][0])-96),sx[0][1],str(ord(sx[0][2])-96)])
	# Part2 - swap first and last letter
	sx[1] = "".join([sx[1][2],sx[1][1],sx[1][0]])
	# Part3 - replace letters with next one in alphabet
	inc = lambda x: "a" if chr(ord(x)+1) == "{" else chr(ord(x)+1)
	sx[2] = "".join([inc(sx[2][i]) for i in range(3)])
	# Final - part2+part3+part1
	return "".join([sx[1],sx[2],sx[0]])

if __name__ == "__main__":
	s = input("Enter password (9 letters long):\n")
	print(secret_password(s))