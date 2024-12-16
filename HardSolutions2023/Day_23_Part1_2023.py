
import heapq
import time
initial = time.time()

grid = [list(line.strip()) for line in open("text.txt","r").readlines()]

def inGrid(pPoint):
    x,y = pPoint

    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

gridDict = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        gridDict[(j,i)] = grid[i][j]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
slopes = ">v<^"
slopeDict = {}
for i in range(len(slopes)):
    slopeDict[slopes[i]] = i

start = (1,0)
end = (len(grid[0]) - 2, len(grid) - 1)

queue = [(0,start,{start})]
weights = []

while queue:
    weight, pos, path = heapq.heappop(queue)

    if pos == end:
        weights.append(weight)

    px,py = pos

    for pInd in range(4):
        dx,dy = dirs[pInd]
        next = (px + dx, py + dy)
 
        if inGrid(next):
            if next not in path:
                currentChar = gridDict[next]

                if currentChar in slopes:
                    if pInd == slopeDict[currentChar]:
                        next = (px + 2 * dx, py + 2 * dy)
                        heapq.heappush(queue, (weight + 2, next, path | {next}))

                elif currentChar == ".":
                    heapq.heappush(queue, (weight + 1, next, path | {next}))

print(max(weights))
