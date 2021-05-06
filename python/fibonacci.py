# Slow

def fib_slow(n:int):
	if n <= 2: return 1
	else: return fib_slow(n-1) + fib_slow(n-2)

# Fast

nums = {}
def fib_fast(n:int):
	if n <= 2: return 1
	if n in nums: return nums[n]
	else:
		num = fib_fast(n-1) + fib_fast(n-2)
		nums[n] = num
		return num

# Mine - I hate recursion and this one is the fastest of all...how ironic.

def fib(n:int):
	a,b = 0,1
	while n > 0:
		n = n - 1
		a,b = b,a+b
	return a