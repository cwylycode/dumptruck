def factor_expression(num:int):
	"""
	Convert a number into it's prime factor representation as an expression. This function turns duplicate values in the expression into exponent versions for optimal viewing.\n
	E.g. - 12 = 2^2x3 (2x2x3), 45 = 3^2x5 (3x3x5), 110 = 2x5x11, 67 = 67 (prime)\n
	More info: https://www.mathsisfun.com/prime-factorization.html
	"""
	def is_prime(i:int):
		if i < 2 or (i % 2 == 0 and i > 2): return False
		for n in range(3,int(i**0.5)+1,2):
			if i % n == 0: return False
		return True
	if num < 2: return str(num)
	n = 2
	f = []
	s = ""
	while 1:
		if is_prime(num):
			f.append(num)
			break
		if not is_prime(n):
			n += 1
			continue
		if (num / n) == (num // n):
			f.append(n)
			num = num // n
		else: n += 1
	dupes = []
	for x in f:
		if x in dupes: continue
		exp = f.count(x)
		if exp > 1:
			s += f"{x}^{exp} x "
			dupes.append(x)
		else: s += f"{x} x "
	return s[0:-3]

if __name__ == "__main__":
	while True:
		i = input("Gimme a whole number:\n")
		print(factor_expression(int(i)))