def avg_multiples(number:int) -> (int,int):
	"""
	Find the two closest whole numbers to each other that multiply into the provided number.
	eg. 72 = 8 * 9 | 50 = 5 * 10 | 43 = 1 * 43 (prime) etc
	"""
	n1,n2 = number,1
	for i in range(2,int(number**0.5)+1):
		if number / i == int(number/i):
			n1 = int(number / i)
			n2 = i
	return n2,n1

if __name__ == "__main__":
	print("Put in a number to get the closest multiples for it\n")
	while True:
		i = int(input())
		print(avg_multiples(i),"\n")