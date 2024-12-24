visited = set()
dirs = [(0,-1),(1,0),(0,1),(-1,0)]

dir = 0
grid = [list(line.strip()) for line in open("text.txt","r").readlines()]
BASE = (0,0)
currentPos = (0,0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            currentPos = (j,i)
            BASE = currentPos
            break

while True:
    visited.add((currentPos,dir))

    nextPos = (currentPos[0] + dirs[dir][0], currentPos[1] + dirs[dir][1])
    if 0 <= nextPos[0] < len(grid[0]) and 0 <= nextPos[1] < len(grid):
        if grid[nextPos[1]][nextPos[0]] == "#":
            dir = (dir + 1)%4
            nextPos = (currentPos[0] + dirs[dir][0], currentPos[1] + dirs[dir][1])
        currentPos = nextPos
    else:

        break

res = set()
for pos, _ in visited:
    res |= {pos}
part1 = len(res)

horiz = {}
vert = {}
obstaclePos = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            obstaclePos.add((j,i))
            try:
                horiz[str(i)].append(j)
            except:
                horiz[str(i)] = [j]
            
            try:
                vert[str(j)].append(i)
            except:
                vert[str(j)] = [i]


for key in horiz.keys():
    horiz[key] = sorted(horiz[key])

for key in vert.keys():
    vert[key] = sorted(vert[key])

part2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        currentPos = BASE
        dir = 0
        visited = set()
        loop = True
 
        horiz[str(i)].append(j)
        vert[str(j)].append(i)
        
        
        horiz[str(i)] = sorted(horiz[str(i)])
        vert[str(j)] = sorted(vert[str(j)])

        while (currentPos,dir) not in visited:
            visited.add((currentPos,dir))
            if dir == 2:
                L = vert[str(currentPos[0])]
                found = False
                for I in range(len(L)):
                    if L[I] > currentPos[1]:
                        currentPos = (currentPos[0], L[I] - 1)
                        dir = (dir + 1) % 4
                        found = True
                        break
                if not found:
                    loop = False
                    break

            elif dir == 0:
                L = vert[str(currentPos[0])]
                found = False
                for I in range(len(L)-1,-1,-1):
                    if L[I] < currentPos[1]:
                        currentPos = (currentPos[0], L[I] + 1)
                        dir = (dir + 1) % 4
                        found = True
                        break
                if not found:
                    loop = False
                    break
            
            elif dir == 1:
                L = horiz[str(currentPos[1])]
                found = False
                for I in range(len(L)):
                    if L[I] > currentPos[0]:
                        currentPos = (L[I] - 1, currentPos[1])
                        dir = (dir + 1) % 4
                        found = True
                        break
                if not found:
                    loop = False
                    break
                
            elif dir == 3:
                L = horiz[str(currentPos[1])]
                found = False
                for I in range(len(L)-1,-1,-1):
                    if L[I] < currentPos[0]:
                        currentPos = (L[I] + 1, currentPos[1])
                        dir = (dir + 1) % 4
                        found = True
                        break
                if not found:
                    loop = False
                    break
 
        horiz[str(i)].remove(j)
        vert[str(j)].remove(i)

        if loop:
            part2 += 1
                
print(f"Part 1: {part1}, Part 2: {part2}")
