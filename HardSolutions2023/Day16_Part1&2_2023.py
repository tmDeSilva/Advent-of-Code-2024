grid = [list(line.strip()) for line in open("text.txt","r")]
GRID = grid

direction = [(1,0),(0,1),(-1,0),(0,-1)]

def add(t1,t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def checkInGrid(p):
    return 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid)

def display(pGrid):
    for line in pGrid:
        print("".join(line))



def light(entryPoint = (0,0),  dir = 0, visited = set()):

    visited = set(visited)

    if (entryPoint,dir) in visited:
        return visited
    
    currentPos = entryPoint
    
    while (currentPos,dir) not in visited:
        visited.add((currentPos,dir))
        currentChar = grid[currentPos[1]][currentPos[0]]

        if currentChar == '\\':
            dir = [1,0,3,2][dir]

        elif currentChar == '/':
            dir = [3,2,1,0][dir]

        elif currentChar == "|" and dir in {0,2}:
            nextPosition = add(currentPos, direction[1])

            if checkInGrid(nextPosition):
                visited |= light(nextPosition, 1, tuple(visited))

            nextPosition = add(currentPos, direction[3])
            if checkInGrid(nextPosition):
                visited |= light(nextPosition, 3, tuple(visited))
            break

        elif currentChar == "-" and dir in {1,3}:
            nextPosition = add(currentPos, direction[0])
            if checkInGrid(nextPosition):
                visited |= light(nextPosition, 0, tuple(visited))

            nextPosition = add(currentPos, direction[2])
            if checkInGrid(nextPosition):
                visited |= light(nextPosition, 2, tuple(visited))
            break

        nextPosition = add(currentPos, direction[dir])

        if checkInGrid(nextPosition):
            currentPos = nextPosition
        else:
            return visited
    
    return visited

import time
initial = time.time()


def getEnergizedSquares(pVisited):
    res = set()
    for pos, _ in pVisited:
        res |= {pos}
    return len(res)

#Part 1, Run time < 0.5s
print(getEnergizedSquares(light()), time.time() - initial)

energized = set()

initial = time.time()
for j in range(0,len(grid[0])):
    energized |= {getEnergizedSquares(light((j,0),1))}
    print(j)
print(time.time() - initial)

initial = time.time()
for j in range(0,len(grid[0])):
    energized |= {getEnergizedSquares(light((j,len(grid) - 1),3))}
    print(j)
print(time.time() - initial)


initial = time.time()
for i in range(0,len(grid)):
    energized |= {getEnergizedSquares(light((0,i),0))}
    print(i)
print(time.time() - initial)

initial = time.time()
for i in range(0,len(grid)):
    energized |= {getEnergizedSquares(light((len(grid[0]) - 1,i),2))}
    print(i)
print(time.time() - initial)

#Part2 Run time < 120s
print(max(energized))
