# Plot out the average multiples that make up a product, both with and without primes being included.

import matplotlib.pyplot as pplot

def avg_multiples(number:int) -> (int,int):
	"""
	Find the two closest whole numbers that multiply into the provided number.
	eg. 72 = 8 * 9 | 50 = 5 * 10 | 43 = 1 * 43 (prime) etc
	"""
	n1,n2 = number,1
	for i in range(2,int(number**0.5)+1):
		if number / i == int(number/i):
			n1 = int(number / i)
			n2 = i
	return n2,n1

amount = 100
data = {i:avg_multiples(i) for i in range(1,amount+1)}
data_filt = dict(filter(lambda x: x[1][1] != x[0] if x[1][1] > 2 else True,data.items()))

pplot.suptitle(f"Average Multiples of Product ({amount} sample)")
ticks = [i for i in range(1,amount+1)]

pplot.subplot(1,2,1)
pplot.title("With Primes")
pplot.xlabel("Products")
pplot.ylabel("Multiples")
pplot.xlim(right=amount+1)
pplot.ylim(top=amount+1)
pplot.plot(list(data.keys()),list(data.values()))

pplot.subplot(1,2,2)
pplot.title("Without Primes")
pplot.xlabel("Products")
pplot.ylabel("Multiples")
pplot.xlim(right=amount+1)
pplot.ylim(top=amount+1)
pplot.plot(list(data_filt.keys()),list(data_filt.values()))

pplot.tight_layout(pad=5, w_pad=1)
pplot.show()