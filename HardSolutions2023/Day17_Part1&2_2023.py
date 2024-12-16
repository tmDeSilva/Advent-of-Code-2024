import heapq
import time
initial = time.time()

grid = [list(map(int,line.strip())) for line in open("text.txt","r").readlines()]

heat = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        heat[(j,i)] = grid[i][j]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
end = (len(grid[0]) - 1, len(grid) - 1)

def inGrid(p):
    x,y = p
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def getHeat(min, max):
    pos = (0,0)
    queue = [(0,pos,0, set()),(0,pos,1, set())]
    visited = set()

    while queue:
        weight, pos, ind, path = heapq.heappop(queue)

        if pos == end:
            return weight
        
        if (pos, ind) in visited:
            continue

        visited |= {(pos,ind)}
    
        visited.add((pos,ind))
        px, py = pos
        for pInd in {0,1,2,3} - {ind, (ind+2)%4}:
            tempWeight = weight
            dx,dy = dirs[pInd]

            tempPath = set()

            for k in range(1, max + 1):
                next = (px + k * dx, py + k * dy)
                
                if inGrid(next) and next not in path:
                    tempPath |= {next}
                    tempWeight += heat[next]
                    if k >= min:
                        heapq.heappush(queue, (tempWeight, next, pInd, path | tempPath))
                else:
                    break


part1 = getHeat(1,3)
part2 = getHeat(4,10)
print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial}")
