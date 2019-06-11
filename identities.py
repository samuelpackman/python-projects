class board:

    def __init__self(self,num_tiles,moves):
        self.num_tiles = num_tiles
        self.moves = moves

    def augment(self):# takes moves and tiles and converts them into sequences of primes




def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1

print(historic(10**3))
