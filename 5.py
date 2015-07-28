def test_factors(output,x):
    for i in xrange(2,x+1):
        if x % i==0 and output*i%x==0:
            return i

output = 1
for x in xrange(20,1,-1):
    output = output * test_factors(output,x) if output % x <> 0 else output

print output
