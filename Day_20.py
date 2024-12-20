import numpy as np
import heapq
import time

initial = time.time()
grid = [list(line.strip()) for line in open("text.txt","r").readlines()]

start = (0,0)
end = (0,0)
part1 = 0
part2 = 0

dirs = set([(1,0),(0,1),(-1,0),(0,-1)])

gridDict = {}
walls = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        gridDict[(j,i)] = grid[i][j]

        if grid[i][j] == "S":
            start = (j,i)
        elif grid[i][j] == "E":
            end = (j,i)
        elif grid[i][j] == "#":
            walls |= {(j,i)}

def inGrid(pPoint):
    x,y = pPoint
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def getPath(pStart, pEnd):
    queue = [(0, pStart, (1,0), [pStart])]
    seen = set()

    while queue:
        weight, pos, currentDir, path = heapq.heappop(queue)

        if pos == pEnd: 
            return path
        
        if (pos,currentDir) in seen:
            continue
        
        seen.add((pos,currentDir))

        for iDir in dirs:
            newWeight = weight
            px,py = pos
            dx,dy = iDir
            next = (px + dx, py + dy)

            if (next,iDir) not in seen and inGrid(next):
                if gridDict[next] != "#":
                    newWeight += 1    
                    heapq.heappush(queue, (newWeight,next,iDir, path + [next]))

pathDict = {}
path = getPath(start,end)

for i in range(len(path)):
    pathDict[path[i]] = i

for i in range(len(path) - 1):
    px, py = path[i]
    for iR in range(2,21):
        for dx,dy in zip(range(-iR, iR+1),range(0, 2*iR+1)):

            if dx > 0:
                dy = 2*iR - dy
    
            for sign in [-1,1]:
                if not(dy == 0 and sign == -1):
                    skipTo = (px + dx, py + sign*dy)

                    if skipTo in pathDict.keys():
                        distance = pathDict[skipTo] - i - iR
                        if distance >= 100:
                            if iR == 2:
                                part1 += 1
                            part2 += 1

print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial:.2f}s")
