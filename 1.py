threes = xrange(0,1000,3)
fives = xrange(0,1000,5)

print sum( set(threes).union(set(fives))  )
