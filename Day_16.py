import numpy as np
import heapq
import time

initial = time.time()
grid = [list(line.strip()) for line in open("text.txt","r").readlines()]

start = (0,0)
end = (0,0)

dirs = set([(1,0),(0,1),(-1,0),(0,-1)])

gridDict = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        gridDict[(j,i)] = grid[i][j]

        if grid[i][j] == "S":
            start = (j,i)
        elif grid[i][j] == "E":
            end = (j,i)

def search(pStart):
    queue = [(0, pStart, (1,0),{pStart})]
    seen = set()
    paths = []

    minWeight = 0
    found = False

    while queue:
        weight, pos, currentDir, path = heapq.heappop(queue)

        if pos == end: 
            if not found:
                minWeight = weight
                found = True
    
            if weight == minWeight:
                paths.append(path)
            else:
                break
                
        seen.add((pos,currentDir))

        for iDir in dirs - {tuple(-np.array(currentDir))}:
            newWeight = weight

            next = tuple(np.array(pos) + np.array(iDir))

            if (next,iDir) not in seen:
                if gridDict[next] != "#":
                    newWeight += 1
                    if iDir != currentDir:
                        newWeight += 1000
   
                    heapq.heappush(queue, (newWeight,next,iDir, path | {next}))

    return minWeight, paths

minWeight, paths = search(start)
part1 = minWeight
bestPos = set()
for iPath in paths:
        bestPos |= iPath

part2 = len(bestPos)
print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial :.2f}s.")
