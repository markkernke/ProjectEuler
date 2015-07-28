
def get_chain(x):
    while x <> 1:
        x = x/2 if x%2==0 else 3*x+1
        yield x

def chain_len(x):
    return sum(1 for x in get_chain(x)) + 1

chains = [ [x,chain_len(x)] for x in xrange(1,1000000) ]
max_x,max_chain_len= 0,0
for chain in chains:
    max_x,max_chain_len = chain[0],chain[1] if chain[1] > max_chain_len else max_x,max_chain_len
