line = list(map(int,open("text.txt","r").read().strip()))

part1Array = []

blocks = []
freespace = []

index = 0
iID = 0
for i in range(len(line)):
    iRange = (index,index+line[i])
    if i % 2 == 1:
        freespace.append(iRange)
        toAdd = -1
    else:
        blocks.append((iID, *iRange))
        toAdd = iID
        iID += 1

    index += line[i]
    part1Array += line[i] * [toAdd]

freespaceCounter = 0
fileCounter = len(part1Array) - 1

while freespaceCounter < fileCounter:
    while part1Array[fileCounter] == -1:
        fileCounter -= 1
    if part1Array[freespaceCounter] == -1:
        part1Array[freespaceCounter] = part1Array[fileCounter]
        part1Array[fileCounter] = -1

    freespaceCounter += 1

part1 = 0
for i in range(len(part1Array)):
    if part1Array[i] != -1:
        part1 += i * part1Array[i]


freespace.append((index,index))

blocks = blocks[::-1]
placedBlocks = []
def f(pBlocks, pSpaces, placed):
    found = False
    ID, blockStart, blockEnd = pBlocks[0]
    for i in range(len(pSpaces)):
        start,end = pSpaces[i]
        if end - start >= blockEnd - blockStart and blockStart >= end:
            placed.append((ID,start,start + blockEnd - blockStart))
            pBlocks.pop(0)
            pSpaces[i] = (start + blockEnd - blockStart, end)
            for j in range(len(pSpaces) - 1, -1,-1):

                if blockEnd == pSpaces[j][0]:
                    pSpaces.insert(j+1,(pSpaces[j-1][0],pSpaces[j][1]))
                    pSpaces.pop(j)
                    pSpaces.pop(j-1)
                    
                    break
            
            found = True
            break

    if not found:
        placed.append(pBlocks.pop(0))

    return pBlocks, pSpaces,placed


while len(blocks) != 0:
    blocks, freespace, placedBlocks = f(blocks, freespace, placedBlocks)

part2 = 0

def t(n):
    return n*(n+1)/2

for a,b,c in placedBlocks:
    part2 += a * (t(c-1)-t(b-1))

part2 = int(part2)
print(f"Part 1: {part1}, Part 2: {part2}")
