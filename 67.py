import requests
grid = [row.split(" ") for row in requests.get('https://projecteuler.net/project/resources/p067_triangle.txt').text.split('\n')]

for x in xrange(len(grid)-3,-1,-1):
    for y in xrange(len(grid[x])):
        grid[x][y] = int(grid[x][y]) + ( int(grid[x+1][y]) if int(grid[x+1][y]) > int(grid[x+1][y+1]) else int(grid[x+1][y+1]) )

print grid[0][0]
