import prime

i = 1
tri = sum(xrange(i))

while prime.num_factors(tri) < 500:
    tri, i = tri+i, i+1

print tri
