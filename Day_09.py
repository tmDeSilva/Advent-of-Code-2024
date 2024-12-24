import numpy as np

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
grid =  [list(map(int,line.strip())) for line in open("text.txt","r").readlines()]
trailheads = []

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 0:
            trailheads.append(np.array((j,i)))

def inGrid(x,y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid[1])

def getPaths(start):
    x,y = start

    count = 0
    res = set()
    current = grid[y][x]
    if current == 9:
        return {(x,y)}, 1 

    found = False
    for delta in [np.array(iDir) for iDir in DIRS]:
        newPos = start + delta
        newX, newY = newPos
        if inGrid(newX,newY):
            if grid[newY][newX] == current + 1:
                found = True
                data = getPaths(newPos)
                res |= data[0]
                count += data[1]
                
    if not found:
        return set(), 0
    
    return res, count

part1 = 0 
part2 = 0
for trailhead in trailheads:
    result = getPaths(trailhead)
    part1 += len(result[0])
    part2 += result[1]

print(f"Part 1: {part1}, Part 2: {part2}.")
