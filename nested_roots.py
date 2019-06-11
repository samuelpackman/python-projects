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

print(primes(5*10**6))
