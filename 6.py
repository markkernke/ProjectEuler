r = xrange(1,101)
sum_of_squares = sum( [ x ** 2 for x in r ] )
square_of_sum = sum(r) ** 2
print square_of_sum - sum_of_squares
