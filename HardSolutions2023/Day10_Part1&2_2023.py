import numpy as np

DIRS = [np.array(iDir) for iDir in [(1,0),(0,1),(-1,0),(0,-1)]]
grid =  [list(line.strip()) for line in open("text.txt","r").readlines()]

pipes = "|-LJ7F"
corners = "LJ7F"
pipesDict = {"|": [(1,1), (3,3)],
        "-": [(0,0), (2,2)],
        "L": [(1,0), (2,3)],
        "J": [(0,3), (1,2)],
        "7": [(0,1), (3,2)],
        "F": [(3,0), (2,1)]}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = np.array((j,i))

finalPath = []

results = set()
for pipe in pipes:
    x,y = start

    dir = pipesDict[pipe][0][1]
    pos = np.array((x,y)) + DIRS[dir]

    path = []
    while tuple(pos) != tuple(start):
        path.append(tuple(pos))
        x,y = pos
        pipe = grid[y][x]
        found = False
        if pipe != ".":
            for initial, final in pipesDict[pipe]:
                if initial == dir:
                    found = True
                    pos += DIRS[final]
                    dir = final
                    break
        if not found:
            break

    path.append(tuple(pos))

    results |= {len(path)//2}
    if len(finalPath) < len(path):
        finalPath = path

part1 = max(results)

part2 = 0
for i in range((length:=len(finalPath))):
    x0, y0 = finalPath[(i-1)%length]
    x1, y1 = finalPath[i]
    x2, y2 = finalPath[(i+1)%length]
    part2 += (1/2) * (y1 + y2) * (x1 - x2)
    
    clockwise = np.matrix([[0, -1],
                [1, 0]])
    anticlockwise = np.matrix([[0, 1],
                [-1, 0]])
    
    delta1 = np.matrix(np.array((x2,y2)) - np.array((x1,y1)))
    delta0 = tuple(np.array((x1,y1)) - np.array((x0,y0)))

    if tuple(np.array((clockwise * (delta1.T)).T)[0]) == delta0:
        part2 -= 3/4
    elif tuple(np.array((anticlockwise * (delta1.T)).T)[0]) == delta0:
        part2 -= 1/4
    else:
        part2 -= 1/2

part2 = int(part2)
print(f"Part 1: {part1}, Part 2: {part2}.")
