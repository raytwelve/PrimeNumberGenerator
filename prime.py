# exploring definition of a prime nubmer; inspired by analyzing Goldbach's conjecture
# Goldbach's Conjecture says that every even number larger than two can be written as the sum of two prime numbers
# !Goldbach: there exists an even number larger than two that cannot be written as the sum of two prime numbers

import math

primes = [2,3,5,7]
break_index = [0]
primes_length = [len(primes)]
last_index = [0]
all_primes_upto = 1000



def findBreak(br, n):
	mid = int(math.sqrt(n))+1

	while br < last_index[0]:
		if primes[br] > mid: break
		br += 1
	return br

def isPrime(n):
	break_index[0] = findBreak(break_index[0], n)

	for i in range(1, break_index[0]+1):
		if n % primes[i] == 0: return False
	primes.append(n)
	primes_length[0] = 1+primes_length[0]
	last_index[0] = 1+ last_index[0]
	# print(last_index[0])
	return True

def main():
	offsets = [1,3,7,9]
	print(primes)

	for i in range(10, all_primes_upto, 10):
		leng = primes_length[0]
		for offset in offsets:
			num = i + offset
			isPrime(num)
		print(primes[leng:])
	# print(primes)




