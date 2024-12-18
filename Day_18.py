import collections
import time
initial = time.time()

rockCoords = [tuple(map(int,line.strip().split(","))) for line in open("text.txt","r").readlines()]
rockSet = set()

dirs = [(1,0), (0,1), (-1,0), (0,-1)]
width = 71
height = 71

end = (width-1,height-1)
def inGrid(pPoint):
    x,y = pPoint
    return 0 <= x < width and 0 <= y < height

def getPath(start = (0,0)):
    queue = collections.deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        pos = path[-1]
        px, py = pos

        if pos == end:
            return path
        
        for dx,dy in dirs:
            next = (px + dx, py + dy)

            if inGrid(next):
                if next not in rockSet and next not in seen:
                    queue.append(path + [next])
                    seen |= {next}

part1 = 0
part2 = 0

for iNumberOfRocks in range(1024,len(rockCoords)):
    
    rockSet = set(rockCoords[:iNumberOfRocks])
    rockThatBlocks = rockCoords[iNumberOfRocks-1]

    res = getPath()
    if iNumberOfRocks == 1024:
        part1 = len(res) - 1

    if res == None:
        part2 = "{0},{1}".format(*rockThatBlocks)
        break

print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial :.2f}s.")
