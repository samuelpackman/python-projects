import math as m
import time



def primes(n):
	if n==2: return [2]
	elif n<2: return []
	s=[i for i in range(3,n+3,2)]
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=int((m*m-3)/2)
			s[j]=0
			while j<half:
				s[j]=0
				j = int(j + m)
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def f(x):
	time_0=time.time()
	prime_list = primes(x)
	length = len(prime_list)
	print(prime_list)
	for numberconsecutive in range(1551,1600,2):
		for i in range(length - numberconsecutive):
			if sum(prime_list[i:i+numberconsecutive]) > x:
					break
			if sum(prime_list[i:i+numberconsecutive]) in prime_list[i+numberconsecutive:]:
				print(numberconsecutive)
				print(sum(prime_list[i:i+numberconsecutive]))
				print(prime_list[i:i+numberconsecutive])


		if sum(prime_list[:numberconsecutive +1]) in prime_list[numberconsecutive:]:
			print(numberconsecutive + 1)
			print(sum(prime_list[:numberconsecutive +1]))
			print((prime_list[:numberconsecutive +1]))


	print(time.time()-time_0)
