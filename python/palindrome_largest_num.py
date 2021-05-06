def largest_palindrome_number(digits:int):
	"""
	Find the largest palindromic (same on both sides) number that is the product of n-digit numbers.\n
	E.g. - 2 digits = 9009 (99*91), 3 digits = 906609 (993*913)\n
	Tip: It is slow to do this, so only use single digits (1-9).
	"""

	start = 10**(digits-1)
	end = 10**(digits-1)*10
	largest = 0

	for n1 in range(end, start - 1, -1):
		for n2 in range(n1, start - 1, -1):
			x = n1 * n2
			if x < largest: break

			# Faster
			if x == int(str(x)[::-1]):
				largest = x

			# Slower
			# num = x
			# rx = 0
			# while num != 0:
			#     rx = rx * 10 + num % 10
			#     num = num // 10
			# if x == rx and x > largest: largest = x

	return largest

if __name__ == "__main__":
	while True:
		i = input("Digits:\n")
		print(largest_palindrome_number(int(i)))