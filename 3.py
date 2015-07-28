n = 600851475143L


#def sieve(limit):
#    a = [True] * limit                          # Initialize the primality list
#    a[0] = a[1] = False
#
#    for (i, isprime) in enumerate(a):
#        if isprime:
#            yield i
#            for n in xrange(i*i, limit, i):     # Mark factors non-prime
#                a[n] = False


#factors = [prime for prime in sieve(goal/2) if goal % prime == 0]

#print max(factors)

i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1

print n
