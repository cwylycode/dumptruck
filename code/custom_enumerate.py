#Super short enumerate example (2-3x slower than the built-in enumerate function)
my_list = ["chess","poodle","boo","hello"]
def enumer(l):return zip([i for i in range(len(l))],l)
for a,b in enumer(my_list):print(f"index: {a}, item: {b}")