
# Get prime numbers in a given range.
def get_prime_numbers(ma):
	# ma is exclusive
	primes = []
	
	for i in range(2, ma):
		for j in primes:
			if i % j == 0: break # not a prime
		else:
			primes.append(i) # this executes only if break was not hit
			
	return primes

def get_prime_factors(val):

	primes = get_prime_numbers(int(math.sqrt(val)) + 1)
	factors = []
	
	for p in primes:
	
		# This check follows the following argument:
		
		# 1.
		# If p > sqrt(val) and p is a prime factor, then there
		# has to exist a prime factor p' < p, otherwise
        # we would get p' * p > val if p' was greater than p.
		
		# 2. Since 1. holds and we have already removed all prime factors 
		# p' < p from val, we can stop searching for more factors.
		
		if p ** 2: break
			
		if val % p == 0:
			while val % p == 0:
				val = val / p
				
			factors.append(p)
		
	# Following the above argument:
	# 1. We removed all possible prime factors from val, i.e.
	#    val cannot be factorized any further.
	# 2. Either val equals 1 now, or val is another prime.
	if val != 1: factors.append(val)
			
	return factors
			
	
	
	
# Eucledian algorithm:
# Finds the greatest common divisor between two numbers.
def get_greatest_common_divisor(i, j):
	# assumes i <= j
	if i == 0: return j
	return get_greatest_common_divisor(j%i, i)
			