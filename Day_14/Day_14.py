import numpy as np
import re
from PIL import Image
import time

instructions = [line.strip() for line in open("text.txt","r").readlines()]

WIDTH = 101
HEIGHT = 103
BATHROOMBREAK = 100
emptyChar = " "
grid = [[emptyChar for i in range(WIDTH)] for j in range(HEIGHT)]
quadrantRobots = [[[] for _ in range(2)] for _ in range(2)]

robotData = []

part1 = 1
part2 = 0
timeElapsed = 0
pattern = "#" * 15
treeFound = False
initialTime = time.time()

def array_to_image(array, cell_size=20):
    rows = len(array)
    cols = len(array[0])
    img = Image.new("RGB", (cols * cell_size, rows * cell_size), "white")
    pixels = img.load()

    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255) if array[row][col] == "#" else (0, 0, 0)
            for i in range(cell_size):
                for j in range(cell_size):
                    pixels[col * cell_size + i, row * cell_size + j] = color
    return img

#Part 1
for line in instructions:
    startX, startY, dx, dy = list(map(int,(re.findall("-?\d+",line))))
    pos = np.array((startX,startY))
    delta = np.array((dx,dy))
    robotData.append((pos,delta))

    for _ in range(BATHROOMBREAK):
        x,y = pos + delta
        pos = np.array((x % WIDTH,y % HEIGHT))

    X,Y = pos
    if not(X == WIDTH//2 or Y == HEIGHT//2):
        i = int(Y > HEIGHT // 2)
        j = int(X > WIDTH // 2)
        quadrantRobots[i][j] = quadrantRobots[i][j] + [tuple(pos)]

for half in quadrantRobots:
    for quadrant in half:
        part1 *= len(quadrant)

#Part 2
while not treeFound:

    timeElapsed += 1
    for i in range(len(robotData)):
        iPos, iDelta = robotData[i]
        x,y = iPos + iDelta
        
        newPos = np.array((x % WIDTH,y % HEIGHT))
        newX, newY = newPos
        grid[newY][newX] = "#"
        robotData[i] = (newPos,iDelta)

    for line in grid:
        if pattern in "".join(line):
            image = array_to_image(grid, cell_size=20)
            image.save(f"tree_{timeElapsed}.png")
            treeFound = True

    grid = [[emptyChar for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
part2 = timeElapsed
print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initialTime:.2f}s.")
