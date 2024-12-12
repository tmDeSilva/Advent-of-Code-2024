import time
import numpy as np

filename = "text.txt"
plants = set("".join(open(filename,"r").read().split("\n")))
grid = [["."] + list(line.strip()) + ["."] for line in open(filename,"r").readlines()]
grid = [["."]* len(grid[0])] + grid + [["."]* len(grid[0])]

dirs = [np.array(iDir) for iDir in [(1,0),(0,-1),(-1,0),(0,1)]]

def findArea(start,char,visited = set()):
    visited |= {start}
 
    for dir in dirs:
        next = tuple(np.array(start) + dir)
        newX, newY = next

        if grid[newY][newX] == char and next not in visited:
            visited |= findArea(next,char,visited)

    return visited

def findPerimeter(pPoints,char):
    pPerimeter = 0
    
    for point in pPoints:
        for dir in dirs:
            x,y = np.array(point) + dir
    
            if grid[y][x] != char:
                pPerimeter += 1

    return pPerimeter

def getSides(pPoints, char):
    pPointsList = sorted(list(pPoints))
    xRange = [min(xs := [j for j,_ in pPointsList]), max(xs) + 1]
    yRange = [min(ys := [i for _,i in pPointsList]), max(ys) + 1]

    sides = 0

    for i in range(*yRange):
        horizontal = [[0,0]]
        for j in range(*xRange):
            if (j,i) in pPointsList:
                exposed = []
                for d in [1,3]:
                    x,y = np.array((j,i)) + dirs[d]
                    exposed.append(1 if grid[y][x] != char else 0)
                horizontal.append(exposed)
            else:
                horizontal.append([0,0])

        for ind in range(len(horizontal)-1):
            if (horizontal[ind][0], horizontal[ind+1][0]) == (0,1):
                sides += 1
            if (horizontal[ind][1], horizontal[ind+1][1]) == (0,1):
                sides += 1

    for j in range(*xRange):
        vertical = [[0,0]]
        for i in range(*yRange):
            if (j,i) in pPointsList:
                exposed = []
                for d in [0,2]:
                    x,y = np.array((j,i)) + dirs[d]
                    exposed.append(1 if grid[y][x] != char else 0)
                vertical.append(exposed)
            else:
                vertical.append([0,0])

        for ind in range(len(vertical)-1):
            if (vertical[ind][0], vertical[ind+1][0]) == (0,1):
                sides += 1
            if (vertical[ind][1], vertical[ind+1][1]) == (0,1):
                sides += 1
        
    return sides

gridPoints = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        gridPoints.append((j,i))

part1 = 0
part2 = 0
seen = set()

initial = time.time()
for plant in plants:
    
    for j,i in gridPoints:
        if grid[i][j] == plant and (j,i) not in seen:
            iRes = findArea((j,i),plant,set())
            
            part1 += (area := len(iRes)) * findPerimeter(iRes,plant)
            part2 += area * getSides(iRes,plant)
            seen |= iRes

print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial:.2f}s.")
