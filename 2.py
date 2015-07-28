fib, old_fib = 1,1
even_fibs = 0
while fib < 4000000:
    fib, old_fib = fib + old_fib, fib
    even_fibs += fib if fib % 2 == 0 else 0

print even_fibs
