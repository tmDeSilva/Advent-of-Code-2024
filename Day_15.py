import numpy as np
import time

initialTime = time.time()
filename = "text.txt"
gridLine, instructions = open(filename,"r").read().split("\n\n")
instructions = "".join(instructions.strip().split("\n"))
gridPart1 = [list(line.strip()) for line in gridLine.split("\n")]
gridPart2 = [list("".join(["@." if element == "@" else "[]" if element == "O" else 2 * element for element in line.strip()])) for line in gridLine.split("\n")]

dirs = [np.array(iDir) for iDir in [(1,0),(0,1),(-1,0),(0,-1)]]
adjacentDirs = [np.array(iDir) for iDir in [(0,0),(1,0),(-1,0)]]
directions = ">v<^"
instructDict = {}
for i in range(len(directions)):
    instructDict[directions[i]] = i

start = (0,0)
rocks = []
solids = set()

part1 = 0
part2 = 0

def getTouchingBoxes(currentBox, pDir):
    touchedBoxes = {currentBox}
    leftHalf,rightHalf = currentBox
    
    leftHalf = np.array(leftHalf) + pDir
    rightHalf = np.array(rightHalf) + pDir
    ends = {tuple(leftHalf),tuple(rightHalf)}

    for iAdjacentDir in adjacentDirs:
        if (potentialBox := (tuple(leftHalf + iAdjacentDir), tuple(rightHalf + iAdjacentDir))) in boxes:
            moreTouchedBoxes, moreEnds = getTouchingBoxes(potentialBox, pDir)
            touchedBoxes |= moreTouchedBoxes
            ends |= moreEnds
    
    return touchedBoxes, ends

for i in range(len(gridPart1)):
    for j in range(len(gridPart1[0])):
        if gridPart1[i][j] == "@":
            start = (j,i)
        if gridPart1[i][j] == "O":
            rocks.append((j,i))
        if gridPart1[i][j] == "#":
            solids.add((j,i))
    
currentPos = np.array(start)

for instruction in instructions:
    currentDir = dirs[instructDict[instruction]]
    nextX, nextY = currentPos + currentDir
    nextPos = (nextX,nextY)

    if nextPos in solids:
        continue
    elif nextPos in rocks:
        rocksToPush = []
        currentRockPos = np.array((nextX,nextY))
        x,y = currentRockPos

        while (x,y) in rocks:
            rocksToPush.append((x,y))
            currentRockPos += currentDir
            x,y = currentRockPos
        
        end = (x,y)
        if end not in solids:
            for rock in rocksToPush:
                rocks.remove(rock)
                newRock = tuple(np.array(rock) + currentDir)
                rocks.append(newRock)

            currentPos = np.array(nextPos)
    else:
        currentPos = np.array(nextPos)
    

for col, row in rocks:
    part1 += 100 * row + col

start = (0,0)
boxes = []
solids = set()

for i in range(len(gridPart2)):
    for j in range(len(gridPart2[0])):
        if gridPart2[i][j] == "@":
            start = (j,i)
        elif gridPart2[i][j] == "[":
            boxes.append(((j,i),(j+1,i)))
        elif gridPart2[i][j] == "#":
            solids |= {(j,i)}

currentPos = np.array(start)


for instruction in instructions:

    dirInd = instructDict[instruction]
    currentDir = dirs[dirInd]
    nextX, nextY = currentPos + currentDir
    nextPos = (nextX,nextY)

    canPush = False

    if nextPos in solids:
        continue

    elif (boxR := (nextPos, (nextX+1,nextY))) in boxes or (boxL := ((nextX-1,nextY) , nextPos)) in boxes:
        touchedBox = ()
        if boxR in boxes:
            touchedBox = boxR
        else:
            touchedBox = boxL

        if dirInd in [0,2]:
            currentRockPos = np.array(nextPos)

            if dirInd == 2:
                currentRockPos += currentDir

            x,y = currentRockPos
            rocksToPush = []
            while (box := ((x,y), (x+1,y))) in boxes:
                rocksToPush.append(box)
                currentRockPos += 2 * currentDir
                x,y = currentRockPos

            if dirInd == 2:
                currentRockPos -= currentDir
                x,y = currentRockPos
                
            end = (x,y)
            if end not in solids:
                canPush = True
            
        else:
            rocksToPush,ends = getTouchingBoxes(touchedBox, currentDir)
            if len(solids.intersection(ends)) == 0:
                canPush = True

        if canPush:
            for box in rocksToPush:
                boxes.remove(box)
                leftHalf,rightHalf = box
                leftHalf = tuple(np.array(leftHalf) + currentDir)
                rightHalf = tuple(np.array(rightHalf) + currentDir)
                boxes.append((leftHalf,rightHalf))

            currentPos = np.array(nextPos)
    else:
        currentPos = np.array(nextPos)

for (col,row),(_,_) in boxes:
    part2 += 100 * row + col

print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initialTime}s.")
