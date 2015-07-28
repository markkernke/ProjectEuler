three_digit = xrange(999,100,-1)


results = xrange(100*100,999*999,1)
palindromes = [x for x in results if str(x) == str(x)[::-1]][::1]

for palindrome in palindromes:
    for num in three_digit:
        if palindrome % num == 0 and palindrome / num in three_digit:
            print palindrome
            exit()
